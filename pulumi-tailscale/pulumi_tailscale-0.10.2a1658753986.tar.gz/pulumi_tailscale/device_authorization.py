# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DeviceAuthorizationArgs', 'DeviceAuthorization']

@pulumi.input_type
class DeviceAuthorizationArgs:
    def __init__(__self__, *,
                 authorized: pulumi.Input[bool],
                 device_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a DeviceAuthorization resource.
        :param pulumi.Input[bool] authorized: Whether or not the device is authorized
        :param pulumi.Input[str] device_id: The device to set as authorized
        """
        pulumi.set(__self__, "authorized", authorized)
        pulumi.set(__self__, "device_id", device_id)

    @property
    @pulumi.getter
    def authorized(self) -> pulumi.Input[bool]:
        """
        Whether or not the device is authorized
        """
        return pulumi.get(self, "authorized")

    @authorized.setter
    def authorized(self, value: pulumi.Input[bool]):
        pulumi.set(self, "authorized", value)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Input[str]:
        """
        The device to set as authorized
        """
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_id", value)


@pulumi.input_type
class _DeviceAuthorizationState:
    def __init__(__self__, *,
                 authorized: Optional[pulumi.Input[bool]] = None,
                 device_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DeviceAuthorization resources.
        :param pulumi.Input[bool] authorized: Whether or not the device is authorized
        :param pulumi.Input[str] device_id: The device to set as authorized
        """
        if authorized is not None:
            pulumi.set(__self__, "authorized", authorized)
        if device_id is not None:
            pulumi.set(__self__, "device_id", device_id)

    @property
    @pulumi.getter
    def authorized(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not the device is authorized
        """
        return pulumi.get(self, "authorized")

    @authorized.setter
    def authorized(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "authorized", value)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[pulumi.Input[str]]:
        """
        The device to set as authorized
        """
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_id", value)


class DeviceAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorized: Optional[pulumi.Input[bool]] = None,
                 device_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The device_authorization resource is used to approve new devices before they can join the tailnet. See https://tailscale.com/kb/1099/device-authorization/ for more details.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tailscale as tailscale

        sample_device = tailscale.get_device(name="device.example.com")
        sample_authorization = tailscale.DeviceAuthorization("sampleAuthorization",
            device_id=sample_device.id,
            authorized=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] authorized: Whether or not the device is authorized
        :param pulumi.Input[str] device_id: The device to set as authorized
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeviceAuthorizationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The device_authorization resource is used to approve new devices before they can join the tailnet. See https://tailscale.com/kb/1099/device-authorization/ for more details.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_tailscale as tailscale

        sample_device = tailscale.get_device(name="device.example.com")
        sample_authorization = tailscale.DeviceAuthorization("sampleAuthorization",
            device_id=sample_device.id,
            authorized=True)
        ```

        :param str resource_name: The name of the resource.
        :param DeviceAuthorizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeviceAuthorizationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorized: Optional[pulumi.Input[bool]] = None,
                 device_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = DeviceAuthorizationArgs.__new__(DeviceAuthorizationArgs)

            if authorized is None and not opts.urn:
                raise TypeError("Missing required property 'authorized'")
            __props__.__dict__["authorized"] = authorized
            if device_id is None and not opts.urn:
                raise TypeError("Missing required property 'device_id'")
            __props__.__dict__["device_id"] = device_id
        super(DeviceAuthorization, __self__).__init__(
            'tailscale:index/deviceAuthorization:DeviceAuthorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authorized: Optional[pulumi.Input[bool]] = None,
            device_id: Optional[pulumi.Input[str]] = None) -> 'DeviceAuthorization':
        """
        Get an existing DeviceAuthorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] authorized: Whether or not the device is authorized
        :param pulumi.Input[str] device_id: The device to set as authorized
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeviceAuthorizationState.__new__(_DeviceAuthorizationState)

        __props__.__dict__["authorized"] = authorized
        __props__.__dict__["device_id"] = device_id
        return DeviceAuthorization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authorized(self) -> pulumi.Output[bool]:
        """
        Whether or not the device is authorized
        """
        return pulumi.get(self, "authorized")

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[str]:
        """
        The device to set as authorized
        """
        return pulumi.get(self, "device_id")

