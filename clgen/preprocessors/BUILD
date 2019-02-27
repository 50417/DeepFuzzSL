# This package defines the preprocessor pipeline for CLgen.

load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")



py_library(
    name = "common",
    srcs = ["common.py"],
    visibility = ["//clgen:__subpackages__"],
    deps = [
        ":public",
        "//clgen:errors",
        "//third_party/py/absl",
    ],
)







py_library(
    name = "preprocessors",
    srcs = ["preprocessors.py"],
    visibility = ["//clgen:__subpackages__"],
    deps = [
        # This target *must* depend on all modules which expose a
        # @public.clgen_preprocessor decorated function, since the method
        # GetPreprocessorFunction() will try to import it. Otherwise it would
        # be the responsibility of any code which calls into one of the public
        # PreprocessX() functions to ensure that the module which implements
        # each preprocessor is listed in its deps.
        ":common",
        ":public",
        "//clgen:errors",
        "//clgen/proto:internal_py_pb2",
        "//third_party/py/absl",
    ],
)


py_library(
    name = "public",
    srcs = ["public.py"],
    visibility = ["//visibility:public"],
    deps = [
        "//third_party/py/absl",
    ],
)
