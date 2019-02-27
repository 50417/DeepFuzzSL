# This package implements the machine learning models for CLgen.

py_library(
    name = "backends",
    srcs = ["backends.py"],
    deps = [
        "//clgen:samplers",
        "//clgen/corpuses:atomizers",
        "//clgen/proto:model_py_pb2",
        "//labm8:cache",
        "//third_party/py/absl",
        "//third_party/py/numpy",
    ],
)

py_library(
    name = "builders",
    srcs = ["builders.py"],
    deps = [
        "//clgen:errors",
        "//clgen/proto:model_py_pb2",
        "//labm8:pbutil",
        "//third_party/py/absl",
        "//third_party/py/keras",
        "//third_party/py/tensorflow",
    ],
)

py_test(
    name = "builders_test",
    srcs = ["builders_test.py"],
    default_python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":builders",
        "//clgen:conftest",
        "//clgen/proto:model_py_pb2",
        "//third_party/py/absl",
        "//third_party/py/pytest",
    ],
)

py_library(
    name = "data_generators",
    srcs = ["data_generators.py"],
    deps = [
        "//clgen:errors",
        "//clgen/proto:model_py_pb2",
        "//third_party/py/absl",
        "//third_party/py/humanize",
        "//third_party/py/numpy",
    ],
)

py_test(
    name = "data_generators_test",
    srcs = ["data_generators_test.py"],
    default_python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":data_generators",
        "//clgen:conftest",
        "//clgen/proto:model_py_pb2",
        "//third_party/py/absl",
        "//third_party/py/pytest",
    ],
)

py_library(
    name = "keras_backend",
    srcs = ["keras_backend.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":backends",
        ":builders",
        ":data_generators",
        "//clgen:samplers",
        "//clgen:telemetry",
        "//clgen/proto:internal_py_pb2",
        "//clgen/proto:model_py_pb2",
        "//clgen/proto:sampler_py_pb2",
        "//labm8:crypto",
        "//labm8:labdate",
        "//labm8:logutil",
        "//labm8:pbutil",
        "//third_party/py/humanize",
        "//third_party/py/keras",
        "//third_party/py/numpy",
        "//third_party/py/tensorflow",
    ],
)

py_test(
    name = "keras_backend_test",
    size = "enormous",
    srcs = ["keras_backend_test.py"],
    default_python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":keras_backend",
        ":models",
        "//clgen:conftest",
        "//clgen/proto:model_py_pb2",
        "//clgen/proto:telemetry_py_pb2",
        "//labm8:crypto",
        "//labm8:fs",
        "//third_party/py/absl",
        "//third_party/py/pytest",
    ],
)

py_library(
    name = "models",
    srcs = ["models.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":builders",
        ":keras_backend",
        ":tensorflow_backend",
        "//clgen:cache",
        "//clgen:errors",
        "//clgen:samplers",
        "//clgen:telemetry",
        "//clgen/corpuses",
        "//clgen/proto:internal_py_pb2",
        "//clgen/proto:model_py_pb2",
        "//clgen/proto:telemetry_py_pb2",
        "//labm8:crypto",
        "//labm8:lockfile",
        "//labm8:pbutil",
        "//third_party/py/absl",
        "//third_party/py/humanize",
        "//third_party/py/numpy",
    ],
)

py_library(
    name = "pretrained",
    srcs = ["pretrained.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":builders",
        ":keras_backend",
        ":tensorflow_backend",
        "//clgen:cache",
        "//clgen:samplers",
        "//clgen:telemetry",
        "//clgen/corpuses:atomizers",
        "//clgen/proto:internal_py_pb2",
        "//clgen/proto:model_py_pb2",
        "//clgen/proto:telemetry_py_pb2",
        "//labm8:cache",
        "//labm8:labdate",
        "//labm8:pbutil",
        "//third_party/py/absl",
        "//third_party/py/humanize",
        "//third_party/py/numpy",
    ],
)

py_test(
    name = "models_test",
    srcs = ["models_test.py"],
    default_python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":models",
        "//clgen:conftest",
        "//clgen/proto:model_py_pb2",
        "//clgen/proto:telemetry_py_pb2",
        "//labm8:crypto",
        "//labm8:fs",
        "//third_party/py/absl",
        "//third_party/py/pytest",
    ],
)

py_library(
    name = "tensorflow_backend",
    srcs = ["tensorflow_backend.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":backends",
        ":builders",
        ":data_generators",
        "//clgen:samplers",
        "//clgen:telemetry",
        "//clgen/proto:internal_py_pb2",
        "//clgen/proto:model_py_pb2",
        "//clgen/proto:sampler_py_pb2",
        "//labm8:crypto",
        "//labm8:labdate",
        "//labm8:logutil",
        "//labm8:pbutil",
        "//third_party/py/absl",
        "//third_party/py/humanize",
        "//third_party/py/numpy",
        "//third_party/py/progressbar",
        "//third_party/py/tensorflow",
    ],
)

py_test(
    name = "tensorflow_backend_test",
    size = "enormous",
    srcs = ["tensorflow_backend_test.py"],
    default_python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":models",
        ":tensorflow_backend",
        "//clgen:conftest",
        "//clgen/proto:model_py_pb2",
        "//clgen/proto:telemetry_py_pb2",
        "//labm8:crypto",
        "//labm8:fs",
        "//third_party/py/absl",
        "//third_party/py/pytest",
    ],
)
