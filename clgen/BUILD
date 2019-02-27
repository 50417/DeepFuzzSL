# This package contains CLgen, a deep learning program generator.
#
# CLgen is an open source application for generating runnable programs using
# deep learning. CLgen learns to program using neural networks which model the
# semantics and usage from large volumes of program fragments, generating
# executable programs that are representative of, but distinct from,
# the programs it learns from.

load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

licenses(["restricted"])  # GPL v3

exports_files([
    "LICENSE",
    "README.md",
])

py_library(
    name = "cache",
    srcs = ["cache.py"],
    visibility = ["//clgen:__subpackages__"],
    deps = [
        "//labm8:cache",
        "//labm8:fs",
        "//third_party/py/absl",
    ],
)

py_binary(
    name = "clgen",
    srcs = ["clgen.py"],
    default_python_version = "PY3",
    srcs_version = "PY3",
    visibility = ["//visibility:public"],
    deps = [
        ":errors",
        ":samplers",
        "//clgen/models",
        "//clgen/models:pretrained",
        "//clgen/proto:clgen_py_pb2",
        "//labm8:pbutil",
        "//labm8:prof",
        "//third_party/py/absl",
    ],
)
py_library(
    name = "errors",
    srcs = ["errors.py"],
    visibility = ["//clgen:__subpackages__"],
)

py3_image(
    name = "clgen_image",
    srcs = ["clgen.py"],
    base = "@base//image",
    main = "clgen.py",
    deps = [
        ":errors",
        ":samplers",
        "//clgen/models",
        "//clgen/proto:clgen_py_pb2",
        "//labm8:pbutil",
        "//labm8:prof",
        "//third_party/py/absl",
    ],
)



py_library(
    name = "conftest",
    testonly = True,
    srcs = ["conftest.py"],
    visibility = ["//visibility:public"],
    deps = [
        "//clgen/proto:clgen_py_pb2",
        "//clgen/proto:corpus_py_pb2",
        "//clgen/proto:model_py_pb2",
        "//clgen/proto:sampler_py_pb2",
        "//labm8:pbutil",
        "//third_party/py/absl",
        "//third_party/py/pytest",
    ],
)


py_binary(
    name = "ls_models",
    srcs = ["ls_models.py"],
    default_python_version = "PY3",
    srcs_version = "PY3",
    visibility = ["//visibility:public"],
    deps = [
        "//clgen/models",
        "//clgen/proto:internal_py_pb2",
        "//labm8:pbutil",
        "//third_party/py/absl",
    ],
)

py_library(
    name = "sample",
    srcs = ["sample.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":errors",
        ":samplers",
        "//clgen/models:pretrained",
        "//clgen/proto:clgen_py_pb2",
        "//labm8:pbutil",
        "//third_party/py/absl",
    ],
)

py_library(
    name = "samplers",
    srcs = ["samplers.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":cache",
        ":errors",
        "//clgen/corpuses:atomizers",
        "//clgen/proto:sampler_py_pb2",
        "//labm8:crypto",
        "//labm8:pbutil",
        "//third_party/py/absl",
    ],
)



py_library(
    name = "telemetry",
    srcs = ["telemetry.py"],
    visibility = ["//visibility:public"],
    deps = [
        "//clgen/proto:telemetry_py_pb2",
        "//labm8:jsonutil",
        "//labm8:labdate",
        "//labm8:pbutil",
        "//third_party/py/absl",
    ],
)
\
