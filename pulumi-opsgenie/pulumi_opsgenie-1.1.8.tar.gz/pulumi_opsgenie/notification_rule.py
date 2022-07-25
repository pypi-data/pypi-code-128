# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['NotificationRuleArgs', 'NotificationRule']

@pulumi.input_type
class NotificationRuleArgs:
    def __init__(__self__, *,
                 action_type: pulumi.Input[str],
                 username: pulumi.Input[str],
                 criterias: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleCriteriaArgs']]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 repeats: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleRepeatArgs']]]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleScheduleArgs']]]] = None,
                 steps: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleStepArgs']]]] = None,
                 time_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleTimeRestrictionArgs']]]] = None):
        """
        The set of arguments for constructing a NotificationRule resource.
        :param pulumi.Input[str] action_type: Type of the action that notification rule will have. Allowed values: `create-alert`, `acknowledged-alert`, `closed-alert`, `assigned-alert`, `add-note`, `schedule-start`, `schedule-end`, `incoming-call-routing`
        :param pulumi.Input[str] username: Username of user to which this notification rule belongs to.
        :param pulumi.Input[bool] enabled: Defined if this step is enabled. Default: `true`
        :param pulumi.Input[str] name: Name of the notification policy
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_times: List of Time Periods that notification for schedule start/end will be sent. Allowed values: `just-before`, `15-minutes-ago`, `1-hour-ago`, `1-day-ago`. If `action_type` is `schedule-start` or `schedule-end` then it is required.
        :param pulumi.Input[int] order: Order of the condition in conditions list
        :param pulumi.Input[Sequence[pulumi.Input['NotificationRuleStepArgs']]] steps: Notification rule steps to take (eg. SMS or email message). This is a block, structure is documented below.
        """
        pulumi.set(__self__, "action_type", action_type)
        pulumi.set(__self__, "username", username)
        if criterias is not None:
            pulumi.set(__self__, "criterias", criterias)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_times is not None:
            pulumi.set(__self__, "notification_times", notification_times)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if repeats is not None:
            pulumi.set(__self__, "repeats", repeats)
        if schedules is not None:
            pulumi.set(__self__, "schedules", schedules)
        if steps is not None:
            pulumi.set(__self__, "steps", steps)
        if time_restrictions is not None:
            pulumi.set(__self__, "time_restrictions", time_restrictions)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[str]:
        """
        Type of the action that notification rule will have. Allowed values: `create-alert`, `acknowledged-alert`, `closed-alert`, `assigned-alert`, `add-note`, `schedule-start`, `schedule-end`, `incoming-call-routing`
        """
        return pulumi.get(self, "action_type")

    @action_type.setter
    def action_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "action_type", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        Username of user to which this notification rule belongs to.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter
    def criterias(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleCriteriaArgs']]]]:
        return pulumi.get(self, "criterias")

    @criterias.setter
    def criterias(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleCriteriaArgs']]]]):
        pulumi.set(self, "criterias", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Defined if this step is enabled. Default: `true`
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the notification policy
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationTimes")
    def notification_times(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Time Periods that notification for schedule start/end will be sent. Allowed values: `just-before`, `15-minutes-ago`, `1-hour-ago`, `1-day-ago`. If `action_type` is `schedule-start` or `schedule-end` then it is required.
        """
        return pulumi.get(self, "notification_times")

    @notification_times.setter
    def notification_times(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "notification_times", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[int]]:
        """
        Order of the condition in conditions list
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter
    def repeats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleRepeatArgs']]]]:
        return pulumi.get(self, "repeats")

    @repeats.setter
    def repeats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleRepeatArgs']]]]):
        pulumi.set(self, "repeats", value)

    @property
    @pulumi.getter
    def schedules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleScheduleArgs']]]]:
        return pulumi.get(self, "schedules")

    @schedules.setter
    def schedules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleScheduleArgs']]]]):
        pulumi.set(self, "schedules", value)

    @property
    @pulumi.getter
    def steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleStepArgs']]]]:
        """
        Notification rule steps to take (eg. SMS or email message). This is a block, structure is documented below.
        """
        return pulumi.get(self, "steps")

    @steps.setter
    def steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleStepArgs']]]]):
        pulumi.set(self, "steps", value)

    @property
    @pulumi.getter(name="timeRestrictions")
    def time_restrictions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleTimeRestrictionArgs']]]]:
        return pulumi.get(self, "time_restrictions")

    @time_restrictions.setter
    def time_restrictions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleTimeRestrictionArgs']]]]):
        pulumi.set(self, "time_restrictions", value)


@pulumi.input_type
class _NotificationRuleState:
    def __init__(__self__, *,
                 action_type: Optional[pulumi.Input[str]] = None,
                 criterias: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleCriteriaArgs']]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 repeats: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleRepeatArgs']]]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleScheduleArgs']]]] = None,
                 steps: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleStepArgs']]]] = None,
                 time_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleTimeRestrictionArgs']]]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NotificationRule resources.
        :param pulumi.Input[str] action_type: Type of the action that notification rule will have. Allowed values: `create-alert`, `acknowledged-alert`, `closed-alert`, `assigned-alert`, `add-note`, `schedule-start`, `schedule-end`, `incoming-call-routing`
        :param pulumi.Input[bool] enabled: Defined if this step is enabled. Default: `true`
        :param pulumi.Input[str] name: Name of the notification policy
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_times: List of Time Periods that notification for schedule start/end will be sent. Allowed values: `just-before`, `15-minutes-ago`, `1-hour-ago`, `1-day-ago`. If `action_type` is `schedule-start` or `schedule-end` then it is required.
        :param pulumi.Input[int] order: Order of the condition in conditions list
        :param pulumi.Input[Sequence[pulumi.Input['NotificationRuleStepArgs']]] steps: Notification rule steps to take (eg. SMS or email message). This is a block, structure is documented below.
        :param pulumi.Input[str] username: Username of user to which this notification rule belongs to.
        """
        if action_type is not None:
            pulumi.set(__self__, "action_type", action_type)
        if criterias is not None:
            pulumi.set(__self__, "criterias", criterias)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_times is not None:
            pulumi.set(__self__, "notification_times", notification_times)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if repeats is not None:
            pulumi.set(__self__, "repeats", repeats)
        if schedules is not None:
            pulumi.set(__self__, "schedules", schedules)
        if steps is not None:
            pulumi.set(__self__, "steps", steps)
        if time_restrictions is not None:
            pulumi.set(__self__, "time_restrictions", time_restrictions)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the action that notification rule will have. Allowed values: `create-alert`, `acknowledged-alert`, `closed-alert`, `assigned-alert`, `add-note`, `schedule-start`, `schedule-end`, `incoming-call-routing`
        """
        return pulumi.get(self, "action_type")

    @action_type.setter
    def action_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_type", value)

    @property
    @pulumi.getter
    def criterias(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleCriteriaArgs']]]]:
        return pulumi.get(self, "criterias")

    @criterias.setter
    def criterias(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleCriteriaArgs']]]]):
        pulumi.set(self, "criterias", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Defined if this step is enabled. Default: `true`
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the notification policy
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationTimes")
    def notification_times(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Time Periods that notification for schedule start/end will be sent. Allowed values: `just-before`, `15-minutes-ago`, `1-hour-ago`, `1-day-ago`. If `action_type` is `schedule-start` or `schedule-end` then it is required.
        """
        return pulumi.get(self, "notification_times")

    @notification_times.setter
    def notification_times(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "notification_times", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[int]]:
        """
        Order of the condition in conditions list
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter
    def repeats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleRepeatArgs']]]]:
        return pulumi.get(self, "repeats")

    @repeats.setter
    def repeats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleRepeatArgs']]]]):
        pulumi.set(self, "repeats", value)

    @property
    @pulumi.getter
    def schedules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleScheduleArgs']]]]:
        return pulumi.get(self, "schedules")

    @schedules.setter
    def schedules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleScheduleArgs']]]]):
        pulumi.set(self, "schedules", value)

    @property
    @pulumi.getter
    def steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleStepArgs']]]]:
        """
        Notification rule steps to take (eg. SMS or email message). This is a block, structure is documented below.
        """
        return pulumi.get(self, "steps")

    @steps.setter
    def steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleStepArgs']]]]):
        pulumi.set(self, "steps", value)

    @property
    @pulumi.getter(name="timeRestrictions")
    def time_restrictions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleTimeRestrictionArgs']]]]:
        return pulumi.get(self, "time_restrictions")

    @time_restrictions.setter
    def time_restrictions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationRuleTimeRestrictionArgs']]]]):
        pulumi.set(self, "time_restrictions", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username of user to which this notification rule belongs to.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class NotificationRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_type: Optional[pulumi.Input[str]] = None,
                 criterias: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleCriteriaArgs']]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 repeats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleRepeatArgs']]]]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleScheduleArgs']]]]] = None,
                 steps: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleStepArgs']]]]] = None,
                 time_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleTimeRestrictionArgs']]]]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Notification Rule within Opsgenie.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_opsgenie as opsgenie

        test_user = opsgenie.User("testUser",
            username="Example user",
            full_name="Name Lastname",
            role="User")
        test_notification_rule = opsgenie.NotificationRule("testNotificationRule",
            username=test_user.username,
            action_type="schedule-end",
            notification_times=[
                "just-before",
                "15-minutes-ago",
            ],
            steps=[opsgenie.NotificationRuleStepArgs(
                contacts=[opsgenie.NotificationRuleStepContactArgs(
                    method="email",
                    to="example@user.com",
                )],
            )])
        ```

        ## Import

        Notification policies can be imported using the `user_id/notification_rule_id`, e.g.

        ```sh
         $ pulumi import opsgenie:index/notificationRule:NotificationRule test user_id/notification_rule_id`
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_type: Type of the action that notification rule will have. Allowed values: `create-alert`, `acknowledged-alert`, `closed-alert`, `assigned-alert`, `add-note`, `schedule-start`, `schedule-end`, `incoming-call-routing`
        :param pulumi.Input[bool] enabled: Defined if this step is enabled. Default: `true`
        :param pulumi.Input[str] name: Name of the notification policy
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_times: List of Time Periods that notification for schedule start/end will be sent. Allowed values: `just-before`, `15-minutes-ago`, `1-hour-ago`, `1-day-ago`. If `action_type` is `schedule-start` or `schedule-end` then it is required.
        :param pulumi.Input[int] order: Order of the condition in conditions list
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleStepArgs']]]] steps: Notification rule steps to take (eg. SMS or email message). This is a block, structure is documented below.
        :param pulumi.Input[str] username: Username of user to which this notification rule belongs to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Notification Rule within Opsgenie.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_opsgenie as opsgenie

        test_user = opsgenie.User("testUser",
            username="Example user",
            full_name="Name Lastname",
            role="User")
        test_notification_rule = opsgenie.NotificationRule("testNotificationRule",
            username=test_user.username,
            action_type="schedule-end",
            notification_times=[
                "just-before",
                "15-minutes-ago",
            ],
            steps=[opsgenie.NotificationRuleStepArgs(
                contacts=[opsgenie.NotificationRuleStepContactArgs(
                    method="email",
                    to="example@user.com",
                )],
            )])
        ```

        ## Import

        Notification policies can be imported using the `user_id/notification_rule_id`, e.g.

        ```sh
         $ pulumi import opsgenie:index/notificationRule:NotificationRule test user_id/notification_rule_id`
        ```

        :param str resource_name: The name of the resource.
        :param NotificationRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotificationRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_type: Optional[pulumi.Input[str]] = None,
                 criterias: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleCriteriaArgs']]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 repeats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleRepeatArgs']]]]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleScheduleArgs']]]]] = None,
                 steps: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleStepArgs']]]]] = None,
                 time_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleTimeRestrictionArgs']]]]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NotificationRuleArgs.__new__(NotificationRuleArgs)

            if action_type is None and not opts.urn:
                raise TypeError("Missing required property 'action_type'")
            __props__.__dict__["action_type"] = action_type
            __props__.__dict__["criterias"] = criterias
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["name"] = name
            __props__.__dict__["notification_times"] = notification_times
            __props__.__dict__["order"] = order
            __props__.__dict__["repeats"] = repeats
            __props__.__dict__["schedules"] = schedules
            __props__.__dict__["steps"] = steps
            __props__.__dict__["time_restrictions"] = time_restrictions
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
        super(NotificationRule, __self__).__init__(
            'opsgenie:index/notificationRule:NotificationRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action_type: Optional[pulumi.Input[str]] = None,
            criterias: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleCriteriaArgs']]]]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            notification_times: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            order: Optional[pulumi.Input[int]] = None,
            repeats: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleRepeatArgs']]]]] = None,
            schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleScheduleArgs']]]]] = None,
            steps: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleStepArgs']]]]] = None,
            time_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleTimeRestrictionArgs']]]]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'NotificationRule':
        """
        Get an existing NotificationRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_type: Type of the action that notification rule will have. Allowed values: `create-alert`, `acknowledged-alert`, `closed-alert`, `assigned-alert`, `add-note`, `schedule-start`, `schedule-end`, `incoming-call-routing`
        :param pulumi.Input[bool] enabled: Defined if this step is enabled. Default: `true`
        :param pulumi.Input[str] name: Name of the notification policy
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_times: List of Time Periods that notification for schedule start/end will be sent. Allowed values: `just-before`, `15-minutes-ago`, `1-hour-ago`, `1-day-ago`. If `action_type` is `schedule-start` or `schedule-end` then it is required.
        :param pulumi.Input[int] order: Order of the condition in conditions list
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NotificationRuleStepArgs']]]] steps: Notification rule steps to take (eg. SMS or email message). This is a block, structure is documented below.
        :param pulumi.Input[str] username: Username of user to which this notification rule belongs to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NotificationRuleState.__new__(_NotificationRuleState)

        __props__.__dict__["action_type"] = action_type
        __props__.__dict__["criterias"] = criterias
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["notification_times"] = notification_times
        __props__.__dict__["order"] = order
        __props__.__dict__["repeats"] = repeats
        __props__.__dict__["schedules"] = schedules
        __props__.__dict__["steps"] = steps
        __props__.__dict__["time_restrictions"] = time_restrictions
        __props__.__dict__["username"] = username
        return NotificationRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Output[str]:
        """
        Type of the action that notification rule will have. Allowed values: `create-alert`, `acknowledged-alert`, `closed-alert`, `assigned-alert`, `add-note`, `schedule-start`, `schedule-end`, `incoming-call-routing`
        """
        return pulumi.get(self, "action_type")

    @property
    @pulumi.getter
    def criterias(self) -> pulumi.Output[Optional[Sequence['outputs.NotificationRuleCriteria']]]:
        return pulumi.get(self, "criterias")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Defined if this step is enabled. Default: `true`
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the notification policy
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationTimes")
    def notification_times(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of Time Periods that notification for schedule start/end will be sent. Allowed values: `just-before`, `15-minutes-ago`, `1-hour-ago`, `1-day-ago`. If `action_type` is `schedule-start` or `schedule-end` then it is required.
        """
        return pulumi.get(self, "notification_times")

    @property
    @pulumi.getter
    def order(self) -> pulumi.Output[int]:
        """
        Order of the condition in conditions list
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter
    def repeats(self) -> pulumi.Output[Optional[Sequence['outputs.NotificationRuleRepeat']]]:
        return pulumi.get(self, "repeats")

    @property
    @pulumi.getter
    def schedules(self) -> pulumi.Output[Optional[Sequence['outputs.NotificationRuleSchedule']]]:
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def steps(self) -> pulumi.Output[Optional[Sequence['outputs.NotificationRuleStep']]]:
        """
        Notification rule steps to take (eg. SMS or email message). This is a block, structure is documented below.
        """
        return pulumi.get(self, "steps")

    @property
    @pulumi.getter(name="timeRestrictions")
    def time_restrictions(self) -> pulumi.Output[Optional[Sequence['outputs.NotificationRuleTimeRestriction']]]:
        return pulumi.get(self, "time_restrictions")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        Username of user to which this notification rule belongs to.
        """
        return pulumi.get(self, "username")

