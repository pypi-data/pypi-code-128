# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ... import meta as _meta
from ._inputs import *

__all__ = ['MutatingWebhookConfigurationPatchArgs', 'MutatingWebhookConfigurationPatch']

@pulumi.input_type
class MutatingWebhookConfigurationPatchArgs:
    def __init__(__self__, *,
                 metadata: pulumi.Input['_meta.v1.ObjectMetaPatchArgs'],
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 webhooks: Optional[pulumi.Input[Sequence[pulumi.Input['MutatingWebhookPatchArgs']]]] = None):
        """
        The set of arguments for constructing a MutatingWebhookConfigurationPatch resource.
        :param pulumi.Input['_meta.v1.ObjectMetaPatchArgs'] metadata: Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input[Sequence[pulumi.Input['MutatingWebhookPatchArgs']]] webhooks: Webhooks is a list of webhooks and the affected resources and operations.
        """
        pulumi.set(__self__, "metadata", metadata)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'admissionregistration.k8s.io/v1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'MutatingWebhookConfiguration')
        if webhooks is not None:
            pulumi.set(__self__, "webhooks", webhooks)

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Input['_meta.v1.ObjectMetaPatchArgs']:
        """
        Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: pulumi.Input['_meta.v1.ObjectMetaPatchArgs']):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def webhooks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MutatingWebhookPatchArgs']]]]:
        """
        Webhooks is a list of webhooks and the affected resources and operations.
        """
        return pulumi.get(self, "webhooks")

    @webhooks.setter
    def webhooks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MutatingWebhookPatchArgs']]]]):
        pulumi.set(self, "webhooks", value)


class MutatingWebhookConfigurationPatch(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaPatchArgs']]] = None,
                 webhooks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MutatingWebhookPatchArgs']]]]] = None,
                 __props__=None):
        """
        Patch resources are used to modify existing Kubernetes resources by using
        Server-Side Apply updates. The name of the resource must be specified, but all other properties are optional. More than
        one patch may be applied to the same resource, and a random FieldManager name will be used for each Patch resource.
        Conflicts will result in an error by default, but can be forced using the "pulumi.com/patchForce" annotation. See the
        [Server-Side Apply Docs](https://www.pulumi.com/registry/packages/kubernetes/installation-configuration/#server-side-apply) for
        additional information about using Server-Side Apply to manage Kubernetes resources with Pulumi.
        MutatingWebhookConfiguration describes the configuration of and admission webhook that accept or reject and may change the object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaPatchArgs']] metadata: Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MutatingWebhookPatchArgs']]]] webhooks: Webhooks is a list of webhooks and the affected resources and operations.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MutatingWebhookConfigurationPatchArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Patch resources are used to modify existing Kubernetes resources by using
        Server-Side Apply updates. The name of the resource must be specified, but all other properties are optional. More than
        one patch may be applied to the same resource, and a random FieldManager name will be used for each Patch resource.
        Conflicts will result in an error by default, but can be forced using the "pulumi.com/patchForce" annotation. See the
        [Server-Side Apply Docs](https://www.pulumi.com/registry/packages/kubernetes/installation-configuration/#server-side-apply) for
        additional information about using Server-Side Apply to manage Kubernetes resources with Pulumi.
        MutatingWebhookConfiguration describes the configuration of and admission webhook that accept or reject and may change the object.

        :param str resource_name: The name of the resource.
        :param MutatingWebhookConfigurationPatchArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MutatingWebhookConfigurationPatchArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaPatchArgs']]] = None,
                 webhooks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MutatingWebhookPatchArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MutatingWebhookConfigurationPatchArgs.__new__(MutatingWebhookConfigurationPatchArgs)

            __props__.__dict__["api_version"] = 'admissionregistration.k8s.io/v1'
            __props__.__dict__["kind"] = 'MutatingWebhookConfiguration'
            if metadata is None and not opts.urn:
                raise TypeError("Missing required property 'metadata'")
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["webhooks"] = webhooks
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="kubernetes:admissionregistration.k8s.io/v1beta1:MutatingWebhookConfigurationPatch")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MutatingWebhookConfigurationPatch, __self__).__init__(
            'kubernetes:admissionregistration.k8s.io/v1:MutatingWebhookConfigurationPatch',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MutatingWebhookConfigurationPatch':
        """
        Get an existing MutatingWebhookConfigurationPatch resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MutatingWebhookConfigurationPatchArgs.__new__(MutatingWebhookConfigurationPatchArgs)

        __props__.__dict__["api_version"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["webhooks"] = None
        return MutatingWebhookConfigurationPatch(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[Optional[str]]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional['_meta.v1.outputs.ObjectMetaPatch']]:
        """
        Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def webhooks(self) -> pulumi.Output[Optional[Sequence['outputs.MutatingWebhookPatch']]]:
        """
        Webhooks is a list of webhooks and the affected resources and operations.
        """
        return pulumi.get(self, "webhooks")

