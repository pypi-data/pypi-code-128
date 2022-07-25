# AUTOGENERATED! DO NOT EDIT! File to edit: 04_DoorGym.ipynb (unless otherwise specified).

__all__ = ['get_validation_args', 'get_training_args', 'eval_print', 'onpolicy_validation', 'mujoco_timestep',
           'onpolicy_main']

# Cell
import os
import sys
import time
import pickle
from collections import deque
import numpy as np
import argparse
import torch
import torch.nn as nn
from tensorboardX import SummaryWriter
import time

from trained_visionmodel.visionmodel import VisionModelXYZ, VisionModel
from a2c_ppo_acktr import algo, utils
from a2c_ppo_acktr.envs import make_vec_envs, VecPyTorch
from a2c_ppo_acktr.model import Policy
from a2c_ppo_acktr.storage import RolloutStorage
from a2c_ppo_acktr.utils import get_vec_normalize, get_render_func

# Cell
def get_validation_args():
    """Create arguments for validation.

    This funcion will build some arguments, like load model, environment and rendered engine.

    Args:
        None.

    Returns:
        The all parameters for validation.

    """
    parser = argparse.ArgumentParser(description='DoorGym validation')
    parser.add_argument(
        '--seed', type=int, default=1, help='random seed (default: 1)')
    parser.add_argument(
        '--log-interval',
        type=int,
        default=10,
        help='log interval, one log per n updates (default: 10)')
    parser.add_argument(
        '--env-name',
        default='doorenv-v0',
        help='environment to train on (default: PongNoFrameskip-v4)')
    parser.add_argument(
        '--non-det',
        action='store_true',
        default=False,
        help='whether to use a non-deterministic policy')
    parser.add_argument(
        '--load-name',
        type=str,
        default='',
        help='which model to load')
    parser.add_argument(
        '--eval',
        action='store_true',
        default=False,
        help="Measure the opening ratio among 100 trials")
    parser.add_argument(
        '--render',
        action='store_true',
        default=False,
        help="force rendering")
    parser.add_argument(
        '--knob-noisy',
        action='store_true',
        default=False,
        help='add noise to knob position to resemble the noise from the visionnet')
    parser.add_argument(
        '--visionnet-input',
        action="store_true",
        default=False,
        help='Use vision net for knob position estimation')
    parser.add_argument(
        '--unity',
        action="store_true",
        default=False,
        help='Use unity for an input of a vision net')
    parser.add_argument(
        '--port',
        type=int,
        default=1050,
        help='Unity connection port (Only for off-policy)')
    parser.add_argument(
        '--visionmodel-path',
        type=str,
        default="./trained_visionmodel/",
        help='load the replay buffer')
    parser.add_argument(
        '--world-path',
        type=str,
        default="/u/home/urakamiy/pytorch-a2c-ppo-acktr-gail/random_world/world/pull_floatinghook",
        help='load the vision network model')
    parser.add_argument(
        '--pos-control',
        action="store_true",
        default=False,
        help='use pos control')
    parser.add_argument(
        '--step-skip',
        type=int,
        default=4,
        help='number of step skip in pos control')
    args = parser.parse_args()

    args.det = not args.non_det

    return args

# Cell
def get_training_args():
    """Create arguments for training.

    This funcion will build some arguments, like algorithm, environment and learning rate.

    Args:
        None.

    Returns:
        The all parameters for training.

    """
    parser = argparse.ArgumentParser(description='DoorGym training')
    parser.add_argument(
        '--algo', default='ppo', help='algorithm to use: a2c | ppo | sac | td3')
    parser.add_argument(
        '--lr', type=float, default=1e-3, help='learning rate (default: 1e-3)')
    parser.add_argument(
        '--eps',
        type=float,
        default=1e-5,
        help='RMSprop optimizer epsilon (default: 1e-5)')
    parser.add_argument(
        '--alpha',
        type=float,
        default=0.99,
        help='RMSprop optimizer apha (default: 0.99)')
    parser.add_argument(
        '--gamma',
        type=float,
        default=0.99,
        help='discount factor for rewards (default: 0.99)')
    parser.add_argument(
        '--use-gae',
        action='store_false',
        default=True,
        help='use generalized advantage estimation')
    parser.add_argument(
        '--gae-lambda',
        type=float,
        default=0.95,
        help='gae lambda parameter (default: 0.95)')
    parser.add_argument(
        '--entropy-coef',
        type=float,
        default=0.01,
        help='entropy term coefficient (default: 0.01)')
    parser.add_argument(
        '--value-loss-coef',
        type=float,
        default=0.5,
        help='value loss coefficient (default: 0.5)')
    parser.add_argument(
        '--max-grad-norm',
        type=float,
        default=0.5,
        help='max norm of gradients (default: 0.5)')
    parser.add_argument(
        '--seed', type=int, default=1, help='random seed (default: 1)')
    parser.add_argument(
        '--cuda-deterministic',
        action='store_true',
        default=False,
        help="sets flags for determinism when using CUDA (potentially slow!)")
    parser.add_argument(
        '--num-processes',
        type=int,
        default=8,
        help='how many training CPU processes to use (default: 8)')
    parser.add_argument(
        '--num-steps',
        type=int,
        default=4096,
        help='number of forward steps (default: 4096)')
    parser.add_argument(
        '--ppo-epoch',
        type=int,
        default=10,
        help='number of ppo epochs (default: 10)')
    parser.add_argument(
        '--num-mini-batch',
        type=int,
        default=256,
        help='number of batches for ppo (default: 256)')
    parser.add_argument(
        '--clip-param',
        type=float,
        default=0.2,
        help='ppo clip parameter (default: 0.2)')
    parser.add_argument(
        '--log-interval',
        type=int,
        default=1,
        help='log interval, one log per n updates (default: 1)')
    parser.add_argument(
        '--save-interval',
        type=int,
        default=5,
        help='save interval, one save per n updates (default: 5)')
    parser.add_argument(
        '--eval-interval',
        type=int,
        default=20,
        help='eval interval, one eval per n updates (default: None)')
    parser.add_argument(
        '--num-env-steps',
        type=int,
        default=10e8,
        help='number of environment steps to train (default: 10e6)')
    parser.add_argument(
        '--env-name',
        default='doorenv-v0',
        help='environment to train on (default: doorenv-v0)')
    parser.add_argument(
        '--log-dir',
        default='./logs/',
        help='directory to save agent logs (default: ./logs/)')
    parser.add_argument(
        '--params-log-dir',
        default='./params_logs/',
        help='directory to save params logs (default: ./params_logs/)')
    parser.add_argument(
        '--save-dir',
        default='./trained_models/',
        help='directory to save agent logs (default: ./trained_models/)')
    parser.add_argument(
        '--no-cuda',
        action='store_true',
        default=False,
        help='disables CUDA training')
    parser.add_argument(
        '--use-proper-time-limits',
        action='store_false',
        default=True,
        help='compute returns taking into account time limits')
    parser.add_argument(
        '--recurrent-policy',
        action='store_true',
        default=False,
        help='use a recurrent policy')
    parser.add_argument(
        '--use-linear-lr-decay',
        action='store_true',
        default=False,
        help='use a linear schedule on the learning rate')
    parser.add_argument(
        '--save-name',
        type=str,
        default="test",
        help='name for changing the log and model name')
    parser.add_argument(
        '--knob-noisy',
        action='store_true',
        default=False,
        help='add noise to knob position to resemble the noise from the visionnet')
    parser.add_argument(
        '--obs-noisy',
        action='store_true',
        default=False,
        help='add noise to entire observation signal')
    parser.add_argument(
        '--pretrained-policy-load',
        type=str,
        default=None,
        help='which pretrained model to load')
    parser.add_argument(
        '--replaybuffer-load',
        type=str,
        default=None,
        help='load the replay buffer')
    parser.add_argument(
        '--visionmodel-path',
        type=str,
        default="./trained_visionmodel/",
        help='load the vision network model')
    parser.add_argument(
        '--world-path',
        type=str,
        default="/home/demo/doorgym/world_generator/world/pull_floatinghook",
        help='load the vision network model')
    parser.add_argument(
        '--val-path',
        type=str,
        default=None,
        help='load the vision network model')
    parser.add_argument(
        '--visionnet-input',
        action="store_true",
        default=False,
        help='Use vision net for knob position estimation')
    parser.add_argument(
        '--unity',
        action="store_true",
        default=False,
        help='Use unity for an input of a vision net')
    parser.add_argument(
        '--port',
        type=int,
        default=1050,
        help='port number to connect to Unity. (Only for SAC)')
    parser.add_argument(
        '--step-skip',
        type=int,
        default=4,
        help='number of step skip in pos control')
    parser.add_argument(
        '--pos-control',
        action="store_true",
        default=False,
        help='Turn on pos control')

    args = parser.parse_args()

    args.cuda = not args.no_cuda and torch.cuda.is_available()

    assert args.algo in ['a2c', 'ppo', 'sac', 'td3']
    if args.recurrent_policy:
        assert args.algo in ['a2c', 'ppo'], \
            'Recurrent policy is not implemented for sac'

    if args.unity:
        assert args.visionnet_input, \
            'Visionnet_input should be True when Unity is True'

    return args

# Cell
mujoco_timestep = 0.02
def eval_print(dooropen_counter, counter, start_time, total_time):
    """Print metric funcion.

    This function will show Average open door time and open door rate.

    Args:
        dooropen_counter :  Success open door conuter.
        counter : The total conuter.
        start_time : Start execute open door time.
        total_time : Total open door time.

    Return :
        opening_rate : Success open door rate.
        opening_timeavg : Average open door time.

    """

    opening_rate = dooropen_counter/counter *100
    if dooropen_counter != 0:
        opening_timeavg = total_time/dooropen_counter
    else:
        opening_timeavg = -1
    print("opening rate {}%. Average time to open is {}.".format(opening_rate, opening_timeavg))
    print("took {}sec to evaluate".format( int(time.mktime(time.localtime())) - start_time ))

    return opening_rate, opening_timeavg

def onpolicy_validation(
                seed,
                env_name,
                det,
                load_name,
                evaluation,
                render,
                knob_noisy,
                visionnet_input,
                env_kwargs,
                actor_critic=None,
                verbose=True,
                pos_control=True,
                step_skip=4):

    """Validation on-policy method

    This function will execute validation trained model.

    Args:
        seed : Setting seed to random.
        env_name : Test Environment.
        det : Whether to use a deterministic policy.
        load_name : Input trained model.
        evaluation : True is evaluation, False is validation.
        render : Whether to render this environment.
        knob_noisy : Whether to add noise into vision.
        visionnet_input : Use vision net to get knob position.
        env_kwargs : Other environment arguments.
        actor_critic : Model network arhitecture.
        verbose : Whether to show opening rate and timeavg.
        pos_control : Whether to use pos control.
        step_skip : The number of step skip in pos control.

    Return:
        opening_rate : Success open door rate.
        opening_timeavg : Average open door time.

    """

    env = make_vec_envs(
        env_name,
        seed + 1000,
        1,
        None,
        None,
        device='cuda:0',
        allow_early_resets=False,
        env_kwargs=env_kwargs,)

    env_obj = env.venv.venv.envs[0].env.env
    if env_name.find('door')<=-1:
        env_obj.unity = None

    render_func = get_render_func(env)
    if evaluation and not render:
        render_func = None

    if env_kwargs['visionnet_input']:
        visionmodel = VisionModelXYZ()
        visionmodel_path = args.visionmodel_path
        if not os.path.isfile(visionmodel_path):
            raise RuntimeError("=> no checkpoint found at '{}'" .format(visionmodel_path))
        checkpoint = torch.load(visionmodel_path)
        visionmodel.load_state_dict(checkpoint['state_dict'])
        best_pred = checkpoint['best_pred']
        print("=> loaded checkpoint '{}' (epoch {}), best pred {}".format(visionmodel_path, checkpoint['epoch'], best_pred))

    if not actor_critic:
            actor_critic, ob_rms = torch.load(load_name)
    actor_critic = actor_critic.eval()
    if env_kwargs['visionnet_input'] and env_name.find('doorenv')>-1:
        actor_critic.visionmodel = visionmodel
        actor_critic.visionnet_input = env_obj.visionnet_input
    actor_critic.to("cuda:0")

    if env_name.find('doorenv')>-1:
        actor_critic.nn = env_obj.nn

    recurrent_hidden_states = torch.zeros(1,actor_critic.recurrent_hidden_state_size)
    masks = torch.zeros(1, 1)

    full_obs = env.reset()
    initial_state = full_obs[:,:env.action_space.shape[0]]

    if env_name.find('doorenv')>-1 and env_obj.visionnet_input:
        obs = actor_critic.obs2inputs(full_obs, 0)
    else:
        if knob_noisy:
            satulation = 100.
            sdv = torch.tensor([3.440133806003181, 3.192113342496682,  1.727412865751099]) /satulation  #Vision SDV for arm
            noise = torch.distributions.Normal(torch.tensor([0.0, 0.0, 0.0]), sdv).sample().cuda()
            noise *= min(1., 100/satulation)
            obs[:,-3:] += noise
        else:
            obs = full_obs

    if render_func is not None:
        render_func('human')

    start_time = int(time.mktime(time.localtime()))

    i=0
    epi_step = 0
    total_time = 0
    epi_counter = 1
    dooropen_counter = 0
    door_opened = False
    test_num = 100

    while True:
        with torch.no_grad():
            value, action, _, recurrent_hidden_states = actor_critic.act(
                obs, recurrent_hidden_states, masks, deterministic=det)
        next_action = action

        if pos_control:
            if i%(512/step_skip-1)==0: current_state = initial_state
            next_action = current_state + next_action
            for kk in range(step_skip):
                full_obs, reward, done, infos = env.step(next_action)

            current_state = full_obs[:,:env.action_space.shape[0]]
        else:
            for kk in range(step_skip):
                full_obs, reward, done, infos = env.step(next_action)


        if env_name.find('doorenv')>-1 and env_obj.visionnet_input:
            obs = actor_critic.obs2inputs(full_obs, 0)
        else:
            if knob_noisy:
                satulation = 100.
                sdv = torch.tensor([3.440133806003181, 3.192113342496682,  1.727412865751099]) /satulation  #Vision SDV for arm
                noise = torch.distributions.Normal(torch.tensor([0.0, 0.0, 0.0]), sdv).sample().cuda()
                noise *= min(1., 100/satulation)
                obs[:,-3:] += noise
            else:
                obs = full_obs

        masks.fill_(0.0 if done else 1.0)

        if render_func is not None:
            render_func('human')

        i+=1
        epi_step += 1

        if env_name.find('doorenv')>-1:
            if not door_opened and abs(env_obj.get_doorangle())>=0.2:
                dooropen_counter += 1
                opening_time = epi_step/(1.0/mujoco_timestep)*step_skip
                if verbose:
                    print("door opened! opening time is {}".format(opening_time))
                total_time += opening_time
                door_opened = True

        if env_name.find('Fetch')>-1:
            if not door_opened and infos[0]['is_success']==1:
                dooropen_counter += 1
                opening_time = epi_step/(1.0/mujoco_timestep)*step_skip
                if verbose:
                    print("Reached destenation! Time is {}".format(opening_time))
                total_time += opening_time
                door_opened = True

        if evaluation:
            if i%(512/step_skip-1)==0:
                if env_obj.unity:
                    env_obj.close()
                env = make_vec_envs(
                env_name,
                seed + 1000,
                1,
                None,
                None,
                device='cuda:0',
                allow_early_resets=False,
                env_kwargs=env_kwargs,)

                if render:
                    render_func = get_render_func(env)
                env_obj = env.venv.venv.envs[0].env.env
                if env_name.find('doorenv')<=-1:
                    env_obj.unity = None
                env.reset()
                if verbose:
                    print("{} ep end >>>>>>>>>>>>>>>>>>>>>>>>".format(epi_counter))
                    eval_print(dooropen_counter, epi_counter, start_time, total_time)
                epi_counter += 1
                epi_step = 0
                door_opened = False


        if i>=512/step_skip*test_num:
            if verbose:
                print( "dooropening counter:",dooropen_counter, " epi counter:", epi_counter)
                eval_print(dooropen_counter, epi_counter-1, start_time, total_time)
            break

    opening_rate, opening_timeavg = eval_print(dooropen_counter, epi_counter-1, start_time, total_time)

    return opening_rate, opening_timeavg

# Cell
def onpolicy_main(args):
    """On-policy training function

    This function will set training environment, including parameters setting, load model, training and evaluation.

    Args:
        Args : The all training parameters.

    Return :
        None.

    """
    print("onpolicy main")

    # torch cuda setting
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    if args.cuda and torch.cuda.is_available() and args.cuda_deterministic:
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True
    torch.set_num_threads(1)
    device = torch.device("cuda:0" if args.cuda else "cpu")

    # tensorboard
    summary_name = args.log_dir + '{0}_{1}'
    writer = SummaryWriter(summary_name.format(args.env_name, args.save_name))

    # create env key word arguments
    env_kwargs = dict(port = args.port,
                    visionnet_input = args.visionnet_input,
                    unity = args.unity,
                    world_path = args.world_path,
                    pos_control = args.pos_control)

    env_kwargs_val = env_kwargs.copy()
    if args.val_path: env_kwargs_val['world_path'] = args.val_path

    # Make vector env
    envs = make_vec_envs(args.env_name,
                         args.seed,
                         args.num_processes,
                         args.gamma,
                         args.log_dir,
                         device,
                         False,
                         env_kwargs=env_kwargs,)

    # agly ways to access to the environment attirubutes
    if args.env_name.find('doorenv')>-1:
        if args.num_processes>1:
            visionnet_input = envs.venv.venv.visionnet_input
            nn = envs.venv.venv.nn
            env_name = envs.venv.venv.xml_path
        else:
            visionnet_input = envs.venv.venv.envs[0].env.env.env.visionnet_input
            nn = envs.venv.venv.envs[0].env.env.env.nn
            env_name = envs.venv.venv.envs[0].env.env.env.xml_path
        # state dimensions
        dummy_obs = np.zeros(23)
    else:
        dummy_obs = envs.observation_space
        visionnet_input = None
        nn = None

    # load pretrained
    if args.pretrained_policy_load:
        print("loading", args.pretrained_policy_load)
        actor_critic, ob_rms = torch.load(args.pretrained_policy_load)
    else:
        actor_critic = Policy(
            dummy_obs.shape,
            envs.action_space,
            base_kwargs={'recurrent': args.recurrent_policy})

    # vision network
    if visionnet_input:
        visionmodel = VisionModelXYZ()
        visionmodel_path = args.visionmodel_path
        if not os.path.isfile(visionmodel_path):
            raise RuntimeError("=> no checkpoint found at '{}'" .format(visionmodel_path))
        checkpoint = torch.load(visionmodel_path)
        visionmodel.load_state_dict(checkpoint['state_dict'])
        best_pred = checkpoint['best_pred']
        print("=> loaded checkpoint '{}' (epoch {}), best pred {}".format(visionmodel_path, checkpoint['epoch'], best_pred))
        actor_critic.visionmodel = visionmodel.eval()

    actor_critic.nn = nn
    actor_critic.to(device)

    #disable normalizer
    vec_norm = get_vec_normalize(envs)
    vec_norm.eval()

    # create agent
    if args.algo == 'a2c':
        agent = algo.A2C_ACKTR(
            actor_critic,
            args.value_loss_coef,
            args.entropy_coef,
            lr=args.lr,
            eps=args.eps,
            alpha=args.alpha,
            max_grad_norm=args.max_grad_norm)
    elif args.algo == 'ppo':
        agent = algo.PPO(
            actor_critic,
            args.clip_param,
            args.ppo_epoch,
            args.num_mini_batch,
            args.value_loss_coef,
            args.entropy_coef,
            lr=args.lr,
            eps=args.eps,
            max_grad_norm=args.max_grad_norm)

    # replay buffer
    rollouts = RolloutStorage(args.num_steps, args.num_processes,
                              dummy_obs.shape, envs.action_space,
                              actor_critic.recurrent_hidden_state_size)

    # get observation
    full_obs = envs.reset()
    initial_state = full_obs[:,:envs.action_space.shape[0]]

    # preprocessing
    if args.env_name.find('doorenv')>-1 and visionnet_input:
        obs = actor_critic.obs2inputs(full_obs, 0)
    else:
        if args.knob_noisy:
            satulation = 100.
            sdv = torch.tensor([3.440133806003181, 3.192113342496682, 1.727412865751099]) /100.  #Vision SDV for arm
            noise = torch.distributions.Normal(torch.tensor([0.0, 0.0, 0.0]), sdv).sample().cuda()
            noise *= min(1., 0/satulation)
            obs[:,-3:] += noise
        elif args.obs_noisy:
            sdv = torch.ones(obs.size(1))*0.03
            noise = torch.distributions.Normal(torch.zeros(sdv.size()), sdv).sample().cuda()
            obs[:] += noise
        else:
            obs = full_obs

    rollouts.obs[0].copy_(obs)
    rollouts.to(device)

    episode_rewards = deque(maxlen=10)

    start = time.time()
    num_updates = int(
        args.num_env_steps) // args.num_steps // args.num_processes

    # training
    for j in range(num_updates):

        if args.use_linear_lr_decay:
            # decrease learning rate linearly
            utils.update_linear_schedule(
                agent.optimizer, j, num_updates, args.lr)

        for step in range(args.num_steps):
            with torch.no_grad():
                value, action, action_log_prob, recurrent_hidden_states = actor_critic.act(
                    rollouts.obs[step], rollouts.recurrent_hidden_states[step],
                    rollouts.masks[step])
                next_action = action

            if args.pos_control:
                if step%(512/args.step_skip-1)==0: current_state = initial_state
                next_action = current_state + next_action
                for kk in range(args.step_skip):
                    full_obs, reward, done, infos = envs.step(next_action)

                current_state = full_obs[:,:envs.action_space.shape[0]]
            else:
                for kk in range(args.step_skip):
                    full_obs, reward, done, infos = envs.step(next_action)

            # convert img to obs if door_env and using visionnet
            if args.env_name.find('doorenv')>-1 and visionnet_input:
                obs = actor_critic.obs2inputs(full_obs, j)
            else:
                if args.knob_noisy:
                    satulation = 100.
                    sdv = torch.tensor([3.440133806003181, 3.192113342496682, 1.727412865751099]) /100.  #Vision SDV for arm
                    noise = torch.distributions.Normal(torch.tensor([0.0, 0.0, 0.0]), sdv).sample().cuda()
                    noise *= min(1., j/satulation)
                    obs[:,-3:] += noise
                elif args.obs_noisy:
                    sdv = torch.ones(obs.size(1))*0.03
                    noise = torch.distributions.Normal(torch.zeros(sdv.size()), sdv).sample().cuda()
                    obs[:] += noise
                else:
                    obs = full_obs

            for info in infos:
                if 'episode' in info.keys():
                    episode_rewards.append(info['episode']['r'])

            masks = torch.FloatTensor(
                [[0.0] if done_ else [1.0] for done_ in done])
            bad_masks = torch.FloatTensor(
                [[0.0] if 'bad_transition' in info.keys() else [1.0]
                 for info in infos])
            rollouts.insert(obs, recurrent_hidden_states, action,
                            action_log_prob, value, reward, masks, bad_masks)

        with torch.no_grad():
            next_value = actor_critic.get_value(
                rollouts.obs[-1], rollouts.recurrent_hidden_states[-1],
                rollouts.masks[-1]).detach()

        rollouts.compute_returns(next_value, args.use_gae, args.gamma,
                                 args.gae_lambda, args.use_proper_time_limits)

        value_loss, action_loss, dist_entropy = agent.update(rollouts)
        rollouts.after_update()

        # Get total number of timesteps
        total_num_steps = (j + 1) * args.num_processes * args.num_steps

        writer.add_scalar("Value loss", value_loss, j)
        writer.add_scalar("action loss", action_loss, j)
        writer.add_scalar("dist entropy loss", dist_entropy, j)
        writer.add_scalar("Episode rewards", np.mean(episode_rewards), j)

        # save for every interval-th episode or for the last epoch
        if (j % args.save_interval == 0
                or j == num_updates - 1) and args.save_dir != "":
            save_path = os.path.join(args.save_dir, args.algo)
            try:
                os.makedirs(save_path)
            except OSError:
                pass
            torch.save([
                actor_critic,
                getattr(utils.get_vec_normalize(envs), 'ob_rms', None)
            ], os.path.join(save_path, args.env_name + "_{}.{}.pt".format(args.save_name,j)))

        if j % args.log_interval == 0 and len(episode_rewards) > 1:
            end = time.time()
            print(
                "Updates {}, num timesteps {}, FPS {} \n Last {} training episodes: mean/median reward {:.1f}/{:.1f}, min/max reward {:.1f}/{:.1f}\n"
                .format(j, total_num_steps,
                        int(total_num_steps / (end - start)),
                        len(episode_rewards), np.mean(episode_rewards),
                        np.median(episode_rewards), np.min(episode_rewards),
                        np.max(episode_rewards), dist_entropy, value_loss,
                        action_loss))
        # evaluation
        if (args.eval_interval is not None and len(episode_rewards) > 1
                and j % args.eval_interval == 0):

            opening_rate, opening_timeavg = onpolicy_validation(
                                                seed=args.seed,
                                                env_name=args.env_name,
                                                det=True,
                                                load_name=args.save_name,
                                                evaluation=True,
                                                render=False,
                                                knob_noisy=args.knob_noisy,
                                                visionnet_input=args.visionnet_input,
                                                env_kwargs=env_kwargs_val,
                                                actor_critic=actor_critic,
                                                verbose=False,
                                                pos_control=args.pos_control,
                                                step_skip=args.step_skip)

            print("{}th update. {}th timestep. opening rate {}%. Average time to open is {}.".format(j, total_num_steps, opening_rate, opening_timeavg))
            writer.add_scalar("Opening rate per envstep", opening_rate, total_num_steps)
            writer.add_scalar("Opening rate per update", opening_rate, j)

        DR=True #Domain Randomization
        ################## for multiprocess world change ######################
        if DR:
            print("changing world")

            envs.close_extras()
            envs.close()
            del envs

            envs = make_vec_envs(args.env_name,
                        args.seed,
                        args.num_processes,
                        args.gamma,
                        args.log_dir,
                        device,
                        False,
                        env_kwargs=env_kwargs,)

            full_obs = envs.reset()
            if args.env_name.find('doorenv')>-1 and visionnet_input:
                obs = actor_critic.obs2inputs(full_obs, j)
            else:
                obs = full_obs
        #######################################################################