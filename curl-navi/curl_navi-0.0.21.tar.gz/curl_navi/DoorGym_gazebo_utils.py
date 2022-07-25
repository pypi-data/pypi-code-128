# AUTOGENERATED! DO NOT EDIT! File to edit: 05_DoorGym_gazebo_inference.ipynb (unless otherwise specified).

__all__ = ['download_model', 'init_model', 'inference']

# Cell
import torch
import os
import gdown
import yaml

# Cell
def download_model(id, path, name):
    """Download a model.

    This function will download model from google cloud.

    Args:
        id : The file id of google cloud.
        path : The path where download model.
        name : The output file name.

    Return:
        model_path : The model path.

    """
    dataset_url = 'https://drive.google.com/u/1/uc?id=' + id
    dataset_name = name + ".pt"
    model_path = os.path.join(path, "model", dataset_name)

    if not os.path.isdir(model_path):
        gdown.download(dataset_url, output = model_path, quiet=False)

    return model_path

# Cell
def init_model(model_path, state_dim):
    """Initial model.

    This function will load model and set need parameters.

    Args:
        model_path : The trained model path.
        state_dim : Dimension of state.

    Return：
        model : After initialization model.

    """
    actor_critic, ob_rms = torch.load(model_path)
    actor_critic = actor_critic.eval()
    actor_critic.nn = state_dim

    return actor_critic

# Cell
def inference(model, state, hidden_state):
    """Inference RL_mm in gazebo or real world.

    This function will use model and state to output next action.

    Args:
        model : The model after initalization.
        state : The environment and robot observation.
        hidden_state : The recurrent network setting.

    Return:
        action : The robot action.
        recurrent_hidden_state : The next hidden_state.

    """
    masks = torch.zeros(1, 1)
    with torch.no_grad():
        _, action, _, recurrent_hidden_states = model.act(
                        state, hidden_state, masks, deterministic=True)

    return action, recurrent_hidden_states