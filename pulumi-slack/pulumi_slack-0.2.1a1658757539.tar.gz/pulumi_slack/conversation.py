# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ConversationArgs', 'Conversation']

@pulumi.input_type
class ConversationArgs:
    def __init__(__self__, *,
                 is_private: pulumi.Input[bool],
                 action_on_destroy: Optional[pulumi.Input[str]] = None,
                 is_archived: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permanent_members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 purpose: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Conversation resource.
        :param pulumi.Input[bool] is_private: create a private channel instead of a public one.
        :param pulumi.Input[str] action_on_destroy: Either of none or archive
        :param pulumi.Input[bool] is_archived: indicates a conversation is archived. Frozen in time.
        :param pulumi.Input[str] name: name of the public or private channel.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permanent_members: user IDs to add to the channel.
        :param pulumi.Input[str] purpose: purpose of the channel.
        :param pulumi.Input[str] topic: topic for the channel.
        """
        pulumi.set(__self__, "is_private", is_private)
        if action_on_destroy is not None:
            pulumi.set(__self__, "action_on_destroy", action_on_destroy)
        if is_archived is not None:
            pulumi.set(__self__, "is_archived", is_archived)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if permanent_members is not None:
            pulumi.set(__self__, "permanent_members", permanent_members)
        if purpose is not None:
            pulumi.set(__self__, "purpose", purpose)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter(name="isPrivate")
    def is_private(self) -> pulumi.Input[bool]:
        """
        create a private channel instead of a public one.
        """
        return pulumi.get(self, "is_private")

    @is_private.setter
    def is_private(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_private", value)

    @property
    @pulumi.getter(name="actionOnDestroy")
    def action_on_destroy(self) -> Optional[pulumi.Input[str]]:
        """
        Either of none or archive
        """
        return pulumi.get(self, "action_on_destroy")

    @action_on_destroy.setter
    def action_on_destroy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_on_destroy", value)

    @property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[bool]]:
        """
        indicates a conversation is archived. Frozen in time.
        """
        return pulumi.get(self, "is_archived")

    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_archived", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the public or private channel.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="permanentMembers")
    def permanent_members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        user IDs to add to the channel.
        """
        return pulumi.get(self, "permanent_members")

    @permanent_members.setter
    def permanent_members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "permanent_members", value)

    @property
    @pulumi.getter
    def purpose(self) -> Optional[pulumi.Input[str]]:
        """
        purpose of the channel.
        """
        return pulumi.get(self, "purpose")

    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "purpose", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        topic for the channel.
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)


@pulumi.input_type
class _ConversationState:
    def __init__(__self__, *,
                 action_on_destroy: Optional[pulumi.Input[str]] = None,
                 created: Optional[pulumi.Input[int]] = None,
                 creator: Optional[pulumi.Input[str]] = None,
                 is_archived: Optional[pulumi.Input[bool]] = None,
                 is_ext_shared: Optional[pulumi.Input[bool]] = None,
                 is_general: Optional[pulumi.Input[bool]] = None,
                 is_org_shared: Optional[pulumi.Input[bool]] = None,
                 is_private: Optional[pulumi.Input[bool]] = None,
                 is_shared: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permanent_members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 purpose: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Conversation resources.
        :param pulumi.Input[str] action_on_destroy: Either of none or archive
        :param pulumi.Input[int] created: is a unix timestamp.
        :param pulumi.Input[str] creator: is the user ID of the member that created this channel.
        :param pulumi.Input[bool] is_archived: indicates a conversation is archived. Frozen in time.
        :param pulumi.Input[bool] is_ext_shared: represents this conversation as being part of a Shared Channel
               with a remote organization.
        :param pulumi.Input[bool] is_general: will be true if this channel is the "general" channel that includes
               all regular team members.
        :param pulumi.Input[bool] is_org_shared: explains whether this shared channel is shared between Enterprise
               Grid workspaces within the same organization.
        :param pulumi.Input[bool] is_private: create a private channel instead of a public one.
        :param pulumi.Input[bool] is_shared: means the conversation is in some way shared between multiple workspaces.
        :param pulumi.Input[str] name: name of the public or private channel.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permanent_members: user IDs to add to the channel.
        :param pulumi.Input[str] purpose: purpose of the channel.
        :param pulumi.Input[str] topic: topic for the channel.
        """
        if action_on_destroy is not None:
            pulumi.set(__self__, "action_on_destroy", action_on_destroy)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if creator is not None:
            pulumi.set(__self__, "creator", creator)
        if is_archived is not None:
            pulumi.set(__self__, "is_archived", is_archived)
        if is_ext_shared is not None:
            pulumi.set(__self__, "is_ext_shared", is_ext_shared)
        if is_general is not None:
            pulumi.set(__self__, "is_general", is_general)
        if is_org_shared is not None:
            pulumi.set(__self__, "is_org_shared", is_org_shared)
        if is_private is not None:
            pulumi.set(__self__, "is_private", is_private)
        if is_shared is not None:
            pulumi.set(__self__, "is_shared", is_shared)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if permanent_members is not None:
            pulumi.set(__self__, "permanent_members", permanent_members)
        if purpose is not None:
            pulumi.set(__self__, "purpose", purpose)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter(name="actionOnDestroy")
    def action_on_destroy(self) -> Optional[pulumi.Input[str]]:
        """
        Either of none or archive
        """
        return pulumi.get(self, "action_on_destroy")

    @action_on_destroy.setter
    def action_on_destroy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_on_destroy", value)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[int]]:
        """
        is a unix timestamp.
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter
    def creator(self) -> Optional[pulumi.Input[str]]:
        """
        is the user ID of the member that created this channel.
        """
        return pulumi.get(self, "creator")

    @creator.setter
    def creator(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creator", value)

    @property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> Optional[pulumi.Input[bool]]:
        """
        indicates a conversation is archived. Frozen in time.
        """
        return pulumi.get(self, "is_archived")

    @is_archived.setter
    def is_archived(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_archived", value)

    @property
    @pulumi.getter(name="isExtShared")
    def is_ext_shared(self) -> Optional[pulumi.Input[bool]]:
        """
        represents this conversation as being part of a Shared Channel
        with a remote organization.
        """
        return pulumi.get(self, "is_ext_shared")

    @is_ext_shared.setter
    def is_ext_shared(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_ext_shared", value)

    @property
    @pulumi.getter(name="isGeneral")
    def is_general(self) -> Optional[pulumi.Input[bool]]:
        """
        will be true if this channel is the "general" channel that includes
        all regular team members.
        """
        return pulumi.get(self, "is_general")

    @is_general.setter
    def is_general(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_general", value)

    @property
    @pulumi.getter(name="isOrgShared")
    def is_org_shared(self) -> Optional[pulumi.Input[bool]]:
        """
        explains whether this shared channel is shared between Enterprise
        Grid workspaces within the same organization.
        """
        return pulumi.get(self, "is_org_shared")

    @is_org_shared.setter
    def is_org_shared(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_org_shared", value)

    @property
    @pulumi.getter(name="isPrivate")
    def is_private(self) -> Optional[pulumi.Input[bool]]:
        """
        create a private channel instead of a public one.
        """
        return pulumi.get(self, "is_private")

    @is_private.setter
    def is_private(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_private", value)

    @property
    @pulumi.getter(name="isShared")
    def is_shared(self) -> Optional[pulumi.Input[bool]]:
        """
        means the conversation is in some way shared between multiple workspaces.
        """
        return pulumi.get(self, "is_shared")

    @is_shared.setter
    def is_shared(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_shared", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the public or private channel.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="permanentMembers")
    def permanent_members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        user IDs to add to the channel.
        """
        return pulumi.get(self, "permanent_members")

    @permanent_members.setter
    def permanent_members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "permanent_members", value)

    @property
    @pulumi.getter
    def purpose(self) -> Optional[pulumi.Input[str]]:
        """
        purpose of the channel.
        """
        return pulumi.get(self, "purpose")

    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "purpose", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        topic for the channel.
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)


class Conversation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_on_destroy: Optional[pulumi.Input[str]] = None,
                 is_archived: Optional[pulumi.Input[bool]] = None,
                 is_private: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permanent_members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 purpose: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Slack channel

        ## Required scopes

        This resource requires the following scopes:

        - [channels:read](https://api.slack.com/scopes/channels:read) (public channels)
        - [channels:manage](https://api.slack.com/scopes/channels:manage) (public channels)
        - [groups:read](https://api.slack.com/scopes/groups:read) (private channels)
        - [groups:write](https://api.slack.com/scopes/groups:write) (private channels)

        The Slack API methods used by the resource are:

        - [conversations.create](https://api.slack.com/methods/conversations.create)
        - [conversations.setTopic](https://api.slack.com/methods/conversations.setTopic)
        - [conversations.setPurpose](https://api.slack.com/methods/conversations.setPurpose)
        - [conversations.info](https://api.slack.com/methods/conversations.info)
        - [conversations.members](https://api.slack.com/methods/conversations.members)
        - [conversations.kick](https://api.slack.com/methods/conversations.kick)
        - [conversations.invite](https://api.slack.com/methods/conversations.invite)
        - [conversations.rename](https://api.slack.com/methods/conversations.rename)
        - [conversations.archive](https://api.slack.com/methods/conversations.archive)
        - [conversations.unarchive](https://api.slack.com/methods/conversations.unarchive)

        If you get `missing_scope` errors while using this resource check the scopes against
        the documentation for the methods above.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_slack as slack

        test = slack.Conversation("test",
            is_private=True,
            permanent_members=[],
            topic="The topic for my channel")
        ```

        ```python
        import pulumi
        import pulumi_slack as slack

        nonadmin = slack.Conversation("nonadmin",
            action_on_destroy="none",
            is_private=True,
            permanent_members=[],
            topic="The channel won't be archived on destroy")
        ```

        ## Import

        `slack_conversation` can be imported using the ID of the conversation/channel, e.g.

        ```sh
         $ pulumi import slack:index/conversation:Conversation my_conversation C023X7QTFHQ
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_on_destroy: Either of none or archive
        :param pulumi.Input[bool] is_archived: indicates a conversation is archived. Frozen in time.
        :param pulumi.Input[bool] is_private: create a private channel instead of a public one.
        :param pulumi.Input[str] name: name of the public or private channel.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permanent_members: user IDs to add to the channel.
        :param pulumi.Input[str] purpose: purpose of the channel.
        :param pulumi.Input[str] topic: topic for the channel.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConversationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Slack channel

        ## Required scopes

        This resource requires the following scopes:

        - [channels:read](https://api.slack.com/scopes/channels:read) (public channels)
        - [channels:manage](https://api.slack.com/scopes/channels:manage) (public channels)
        - [groups:read](https://api.slack.com/scopes/groups:read) (private channels)
        - [groups:write](https://api.slack.com/scopes/groups:write) (private channels)

        The Slack API methods used by the resource are:

        - [conversations.create](https://api.slack.com/methods/conversations.create)
        - [conversations.setTopic](https://api.slack.com/methods/conversations.setTopic)
        - [conversations.setPurpose](https://api.slack.com/methods/conversations.setPurpose)
        - [conversations.info](https://api.slack.com/methods/conversations.info)
        - [conversations.members](https://api.slack.com/methods/conversations.members)
        - [conversations.kick](https://api.slack.com/methods/conversations.kick)
        - [conversations.invite](https://api.slack.com/methods/conversations.invite)
        - [conversations.rename](https://api.slack.com/methods/conversations.rename)
        - [conversations.archive](https://api.slack.com/methods/conversations.archive)
        - [conversations.unarchive](https://api.slack.com/methods/conversations.unarchive)

        If you get `missing_scope` errors while using this resource check the scopes against
        the documentation for the methods above.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_slack as slack

        test = slack.Conversation("test",
            is_private=True,
            permanent_members=[],
            topic="The topic for my channel")
        ```

        ```python
        import pulumi
        import pulumi_slack as slack

        nonadmin = slack.Conversation("nonadmin",
            action_on_destroy="none",
            is_private=True,
            permanent_members=[],
            topic="The channel won't be archived on destroy")
        ```

        ## Import

        `slack_conversation` can be imported using the ID of the conversation/channel, e.g.

        ```sh
         $ pulumi import slack:index/conversation:Conversation my_conversation C023X7QTFHQ
        ```

        :param str resource_name: The name of the resource.
        :param ConversationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConversationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_on_destroy: Optional[pulumi.Input[str]] = None,
                 is_archived: Optional[pulumi.Input[bool]] = None,
                 is_private: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permanent_members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 purpose: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConversationArgs.__new__(ConversationArgs)

            __props__.__dict__["action_on_destroy"] = action_on_destroy
            __props__.__dict__["is_archived"] = is_archived
            if is_private is None and not opts.urn:
                raise TypeError("Missing required property 'is_private'")
            __props__.__dict__["is_private"] = is_private
            __props__.__dict__["name"] = name
            __props__.__dict__["permanent_members"] = permanent_members
            __props__.__dict__["purpose"] = purpose
            __props__.__dict__["topic"] = topic
            __props__.__dict__["created"] = None
            __props__.__dict__["creator"] = None
            __props__.__dict__["is_ext_shared"] = None
            __props__.__dict__["is_general"] = None
            __props__.__dict__["is_org_shared"] = None
            __props__.__dict__["is_shared"] = None
        super(Conversation, __self__).__init__(
            'slack:index/conversation:Conversation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action_on_destroy: Optional[pulumi.Input[str]] = None,
            created: Optional[pulumi.Input[int]] = None,
            creator: Optional[pulumi.Input[str]] = None,
            is_archived: Optional[pulumi.Input[bool]] = None,
            is_ext_shared: Optional[pulumi.Input[bool]] = None,
            is_general: Optional[pulumi.Input[bool]] = None,
            is_org_shared: Optional[pulumi.Input[bool]] = None,
            is_private: Optional[pulumi.Input[bool]] = None,
            is_shared: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            permanent_members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            purpose: Optional[pulumi.Input[str]] = None,
            topic: Optional[pulumi.Input[str]] = None) -> 'Conversation':
        """
        Get an existing Conversation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_on_destroy: Either of none or archive
        :param pulumi.Input[int] created: is a unix timestamp.
        :param pulumi.Input[str] creator: is the user ID of the member that created this channel.
        :param pulumi.Input[bool] is_archived: indicates a conversation is archived. Frozen in time.
        :param pulumi.Input[bool] is_ext_shared: represents this conversation as being part of a Shared Channel
               with a remote organization.
        :param pulumi.Input[bool] is_general: will be true if this channel is the "general" channel that includes
               all regular team members.
        :param pulumi.Input[bool] is_org_shared: explains whether this shared channel is shared between Enterprise
               Grid workspaces within the same organization.
        :param pulumi.Input[bool] is_private: create a private channel instead of a public one.
        :param pulumi.Input[bool] is_shared: means the conversation is in some way shared between multiple workspaces.
        :param pulumi.Input[str] name: name of the public or private channel.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] permanent_members: user IDs to add to the channel.
        :param pulumi.Input[str] purpose: purpose of the channel.
        :param pulumi.Input[str] topic: topic for the channel.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConversationState.__new__(_ConversationState)

        __props__.__dict__["action_on_destroy"] = action_on_destroy
        __props__.__dict__["created"] = created
        __props__.__dict__["creator"] = creator
        __props__.__dict__["is_archived"] = is_archived
        __props__.__dict__["is_ext_shared"] = is_ext_shared
        __props__.__dict__["is_general"] = is_general
        __props__.__dict__["is_org_shared"] = is_org_shared
        __props__.__dict__["is_private"] = is_private
        __props__.__dict__["is_shared"] = is_shared
        __props__.__dict__["name"] = name
        __props__.__dict__["permanent_members"] = permanent_members
        __props__.__dict__["purpose"] = purpose
        __props__.__dict__["topic"] = topic
        return Conversation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionOnDestroy")
    def action_on_destroy(self) -> pulumi.Output[Optional[str]]:
        """
        Either of none or archive
        """
        return pulumi.get(self, "action_on_destroy")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[int]:
        """
        is a unix timestamp.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def creator(self) -> pulumi.Output[str]:
        """
        is the user ID of the member that created this channel.
        """
        return pulumi.get(self, "creator")

    @property
    @pulumi.getter(name="isArchived")
    def is_archived(self) -> pulumi.Output[Optional[bool]]:
        """
        indicates a conversation is archived. Frozen in time.
        """
        return pulumi.get(self, "is_archived")

    @property
    @pulumi.getter(name="isExtShared")
    def is_ext_shared(self) -> pulumi.Output[bool]:
        """
        represents this conversation as being part of a Shared Channel
        with a remote organization.
        """
        return pulumi.get(self, "is_ext_shared")

    @property
    @pulumi.getter(name="isGeneral")
    def is_general(self) -> pulumi.Output[bool]:
        """
        will be true if this channel is the "general" channel that includes
        all regular team members.
        """
        return pulumi.get(self, "is_general")

    @property
    @pulumi.getter(name="isOrgShared")
    def is_org_shared(self) -> pulumi.Output[bool]:
        """
        explains whether this shared channel is shared between Enterprise
        Grid workspaces within the same organization.
        """
        return pulumi.get(self, "is_org_shared")

    @property
    @pulumi.getter(name="isPrivate")
    def is_private(self) -> pulumi.Output[bool]:
        """
        create a private channel instead of a public one.
        """
        return pulumi.get(self, "is_private")

    @property
    @pulumi.getter(name="isShared")
    def is_shared(self) -> pulumi.Output[bool]:
        """
        means the conversation is in some way shared between multiple workspaces.
        """
        return pulumi.get(self, "is_shared")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        name of the public or private channel.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="permanentMembers")
    def permanent_members(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        user IDs to add to the channel.
        """
        return pulumi.get(self, "permanent_members")

    @property
    @pulumi.getter
    def purpose(self) -> pulumi.Output[Optional[str]]:
        """
        purpose of the channel.
        """
        return pulumi.get(self, "purpose")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[Optional[str]]:
        """
        topic for the channel.
        """
        return pulumi.get(self, "topic")

