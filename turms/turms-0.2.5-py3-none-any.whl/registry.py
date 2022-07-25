import ast
from typing import Dict, List
from turms.config import GeneratorConfig
from keyword import iskeyword
from turms.errors import (
    NoEnumFound,
    NoInputTypeFound,
    NoScalarFound,
    RegistryError,
)
from turms.stylers.base import Styler
from rich import get_console

SCALAR_DEFAULTS = {
    "ID": "str",
    "String": "str",
    "Int": "int",
    "Boolean": "bool",
    "GenericScalar": "typing.Dict",
    "DateTime": "str",
    "Float": "float",
}


built_in_map = {
    "__TypeKind": ast.ClassDef(
        "__TypeKind",
        bases=[
            ast.Name(id="str", ctx=ast.Load()),
            ast.Name(id="Enum", ctx=ast.Load()),
        ],
        decorator_list=[],
        keywords=[],
        body=[
            ast.Assign(
                targets=[ast.Name(id=str(value), ctx=ast.Store())],
                value=ast.Constant(value=value),
            )
            for value in ["OBJECT", "INTERFACE", "UNION", "ENUM", "INPUT_OBJECT"]
        ],
    ),
    "__DirectiveLocation": ast.ClassDef(
        "__DirectiveLocation",
        bases=[
            ast.Name(id="str", ctx=ast.Load()),
            ast.Name(id="Enum", ctx=ast.Load()),
        ],
        decorator_list=[],
        keywords=[],
        body=[
            ast.Assign(
                targets=[ast.Name(id=str(value), ctx=ast.Store())],
                value=ast.Constant(value=value),
            )
            for value in [
                "SCALAR",
                "OBJECT",
                "FIELD_DEFINITION",
                "ARGUMENT_DEFINITION",
                "INTERFACE",
                "UNION",
                "ENUM",
                "ENUM_VALUE",
                "INPUT_OBJECT",
                "INPUT_FIELD_DEFINITION",
                "SCHEMA",
            ]
        ],
    ),
}


class ClassRegistry(object):
    def __init__(self, config: GeneratorConfig, stylers: List[Styler]):
        self.stylers = stylers
        self._imports = set()
        self._builtins = set()
        self.config = config

        self.scalar_map = {**SCALAR_DEFAULTS, **config.scalar_definitions}

        self.fragment_document_map = {}

        self.enum_class_map = {}
        self.inputtype_class_map = {}
        self.object_class_map = {}
        self.interface_reference_map = {}
        self.interface_baseclass_map = {}

        self.operation_class_map = {}
        self.fragment_class_map = {}
        self.query_class_map = {}
        self.subscription_class_map = {}
        self.mutation_class_map = {}

        self.forward_references = set()

        self.interfacefragments_class_map = {}
        self.console = get_console()

    def style_inputtype_class(self, typename: str):
        for styler in self.stylers:
            typename = styler.style_input_name(typename)
        if iskeyword(typename):
            typename += "_"
        return typename

    def generate_inputtype(self, typename: str):
        assert (
            typename not in self.inputtype_class_map
        ), "Type was already registered, cannot register annew"
        classname = self.style_inputtype_class(typename)
        self.inputtype_class_map[typename] = classname
        return classname

    def get_inputtype_class(self, typename) -> str:
        return self.inputtype_class_map[typename]

    def reference_inputtype(
        self, typename: str, parent: str, allow_forward=True
    ) -> ast.AST:
        classname = self.style_inputtype_class(typename)
        if typename not in self.inputtype_class_map or parent == classname:
            if not allow_forward:
                raise NoInputTypeFound(
                    f"Input type {typename} is not yet defined but referenced by {parent}. And we dont allow forward references"
                )
            self.forward_references.add(parent)
            return ast.Constant(value=classname, ctx=ast.Load())
        return ast.Name(id=self.inputtype_class_map[typename], ctx=ast.Load())

    def style_enum_class(self, typename: str):
        for styler in self.stylers:
            typename = styler.style_enum_name(typename)
        if iskeyword(typename):
            typename += "_"
        return typename

    def generate_enum(self, typename: str):
        assert (
            typename not in self.enum_class_map
        ), "Type was already registered, cannot register annew"
        classname = self.style_enum_class(typename)
        self.enum_class_map[typename] = classname
        return classname

    def get_enum_class(self, typename) -> str:
        return self.enum_class_map[typename]

    def reference_enum(self, typename: str, parent: str, allow_forward=True) -> ast.AST:
        if typename in built_in_map:
            # Builtin enums
            self._builtins.add(typename)
            self.forward_references.add(parent)
            return ast.Constant(value=typename, ctx=ast.Load())

        classname = self.style_enum_class(typename)
        if typename not in self.enum_class_map or parent == classname:
            if not allow_forward:
                raise NoEnumFound(
                    f"Input type {typename} is not yet defined but referenced by {parent}. And we dont allow forward references"
                )
            self.forward_references.add(parent)
            return ast.Constant(value=classname, ctx=ast.Load())
        return ast.Name(id=classname, ctx=ast.Load())

    def style_objecttype_class(self, typename: str):
        for styler in self.stylers:
            typename = styler.style_object_name(typename)
        if iskeyword(typename):
            typename += "_"
        return typename

    def generate_objecttype(self, typename: str):
        assert (
            typename not in self.object_class_map
        ), "Type was already registered, cannot register annew"
        classname = self.style_objecttype_class(typename)
        self.object_class_map[typename] = classname
        return classname

    def reference_object(
        self, typename: str, parent: str, allow_forward=True
    ) -> ast.AST:
        return self._reference_generic(
            typename,
            parent,
            self.style_objecttype_class,
            self.object_class_map,
            "Object",
            allow_forward,
        )

    def _reference_generic(
        self,
        typename: str,
        parent: str,
        styler,
        class_map: Dict,
        error_class: str,
        allow_forward=True,
    ) -> ast.AST:
        classname = styler(typename)
        if typename not in class_map or parent == classname:
            if not allow_forward:
                raise RegistryError(
                    f"""{error_class} type {typename} is not yet defined but referenced by {parent}. And we dont allow forward references"""
                )
            self.forward_references.add(parent)
            return ast.Constant(value=classname, ctx=ast.Load())
        return ast.Name(id=classname, ctx=ast.Load())

    def style_interface_class(self, typename: str):
        for styler in self.stylers:
            typename = styler.style_object_name(typename)
        if iskeyword(typename):
            typename += "_"
        return typename

    def generate_interface(self, typename: str):
        assert (
            typename not in self.interface_baseclass_map
        ), "Type was already registered, cannot register annew"
        classname = self.style_interface_class(typename)
        self.interface_baseclass_map[typename] = classname + "Base"
        self.interface_reference_map[typename] = classname
        return classname + "Base"

    def inherit_interface(self, typename: str, allow_forward=True) -> ast.AST:
        if typename not in self.interface_baseclass_map:
            raise RegistryError(
                f"Interface type {typename} is not yet defined but referenced by. And we dont allow forward references"
            )
        return self.interface_baseclass_map[typename]

    def reference_interface(
        self, typename: str, parent: str, allow_forward=True
    ) -> ast.AST:
        # Interface need always be udpated later
        classname = self.style_interface_class(typename)
        self.forward_references.add(parent)
        return ast.Constant(value=classname, ctx=ast.Load())

    def style_fragment_class(self, typename: str):
        for styler in self.stylers:
            typename = styler.style_fragment_name(typename)
        if iskeyword(typename):
            typename += "_"
        return typename

    def generate_fragment(self, typename: str):
        assert (
            typename not in self.fragment_class_map
        ), f"Type {typename} was already registered, cannot register annew"
        classname = self.style_fragment_class(typename)
        self.fragment_class_map[typename] = classname
        return classname

    def reference_fragment(
        self, typename: str, parent: str, allow_forward=True
    ) -> ast.AST:
        return self._reference_generic(
            typename,
            parent,
            self.style_fragment_class,
            self.fragment_class_map,
            "Fragment",
            allow_forward,
        )

    def inherit_fragment(self, typename: str, allow_forward=True) -> ast.AST:
        if typename not in self.fragment_class_map:
            raise RegistryError(
                f"Interface type {typename} is not yet defined but referenced by. And we dont allow forward references"
            )
        return self.fragment_class_map[typename]

    def generate_node_name(self, node_name: str):
        for styler in self.stylers:
            node_name = styler.style_node_name(node_name)

        if iskeyword(node_name):
            return node_name + "_"

        return node_name

    def generate_parameter_name(self, node_name: str):
        for styler in self.stylers:
            node_name = styler.style_parameter_name(node_name)

        if iskeyword(node_name):
            return node_name + "_"

        return node_name

    def style_query_class(self, typename: str):
        for styler in self.stylers:
            typename = styler.style_query_name(typename)
        if iskeyword(typename):
            typename += "_"
        return typename

    def generate_query(self, typename: str):
        assert (
            typename not in self.query_class_map
        ), f"Type {typename} was already registered, cannot register annew"
        classname = self.style_query_class(typename)
        self.query_class_map[typename] = classname
        return classname

    def reference_query(
        self, typename: str, parent: str, allow_forward=True
    ) -> ast.AST:
        return self._reference_generic(
            typename,
            parent,
            self.style_query_class,
            self.query_class_map,
            "Query",
            allow_forward,
        )

    def style_mutation_class(self, typename: str):
        for styler in self.stylers:
            typename = styler.style_mutation_name(typename)
        if iskeyword(typename):
            typename += "_"
        return typename

    def generate_mutation(self, typename: str):
        assert (
            typename not in self.mutation_class_map
        ), f"Type {typename} was already registered, cannot register annew"
        classname = self.style_mutation_class(typename)
        self.mutation_class_map[typename] = classname
        return classname

    def reference_mutation(
        self, typename: str, parent: str, allow_forward=True
    ) -> ast.AST:
        return self._reference_generic(
            typename,
            parent,
            self.style_mutation_class,
            self.mutation_class_map,
            "Mutation",
            allow_forward,
        )

    def style_subscription_class(self, typename: str):
        for styler in self.stylers:
            typename = styler.style_subscription_name(typename)
        if iskeyword(typename):
            typename += "_"
        return typename

    def generate_subscription(self, typename: str):
        assert (
            typename not in self.subscription_class_map
        ), f"Type {typename} was already registered, cannot register annew"
        classname = self.style_subscription_class(typename)
        self.subscription_class_map[typename] = classname
        return classname

    def reference_subscription(
        self, typename: str, parent: str, allow_forward=True
    ) -> ast.AST:
        return self._reference_generic(
            typename,
            parent,
            self.style_subscription_class,
            self.subscription_class_map,
            "Subscription",
            allow_forward,
        )

    def register_import(self, name):
        if name in ("bool", "str", "int", "float", "dict", "list", "tuple"):
            return

        assert "." in name, "Please only register imports with a top level package"
        self._imports.add(name)

    def generate_imports(self):
        imports = []

        top_level = {}
        for name in self._imports:
            top_level.setdefault(".".join(name.split(".")[:-1]), set()).add(
                name.split(".")[-1]
            )

        for top_level_name, sub_level_names in top_level.items():
            imports.append(
                ast.ImportFrom(
                    module=top_level_name,
                    names=[ast.alias(name=name) for name in sub_level_names],
                    level=0,
                )
            )

        return imports

    def generate_builtins(self):
        builtins = []

        for built_in in self._builtins:
            builtins.append(built_in_map[built_in])

        return builtins

    def generate_forward_refs(self):
        tree = []

        for reference in sorted(self.forward_references):
            tree.append(
                ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(
                                id=reference,
                                ctx=ast.Load(),
                            ),
                            attr="update_forward_refs",
                            ctx=ast.Load(),
                        ),
                        keywords=[],
                        args=[],
                    )
                )
            )

        return tree

    def register_fragment_document(self, typename: str, cls: str):
        assert cls not in self.fragment_document_map, f"{cls} already registered"
        self.fragment_document_map[typename] = cls

    def get_fragment_document(self, typename: str):
        return self.fragment_document_map[typename]

    def reference_scalar(self, scalar_type: str):
        if scalar_type in self.scalar_map:
            python_type = self.scalar_map[scalar_type]
            if "." in python_type:
                # We make the assumption that the scalar type is a fully qualified class name
                self.register_import(python_type)

            return ast.Name(
                id=python_type.split(".")[-1], ctx=ast.Load()
            )  # That results only in the class name (also in the case of a builtin)

        raise NoScalarFound(
            f"No python equivalent found for {scalar_type}. Please define in scalar_definitions"
        )

    def warn(self, message):
        self.console.print("[r]" + message)
