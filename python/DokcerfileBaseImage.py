from typing import TYPE_CHECKING

from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.dockerfile.base_dockerfile_check import BaseDockerfileCheck

AUTHORIZED_REGISTRIES = ["gcr.io", "ghcr.com"]

if TYPE_CHECKING:
    from dockerfile_parse.parser import _Instruction


class CheckBaseImage(BaseDockerfileCheck):
    def __init__(self) -> None:
        name = "Ensure that Dockerfile is using authorized Base Image only"
        id = "CKV_DOCKER_CUSTOM_100"
        supported_instructions = ("FROM",)
        categories = (CheckCategories.APPLICATION_SECURITY,)
        guideline = f"You should use only authorized base images from {', '.join(AUTHORIZED_REGISTRIES)}"
        super().__init__(name=name, id=id, categories=categories,
                         supported_instructions=supported_instructions, guideline=guideline)

    def scan_resource_conf(self, conf):
        for base_images in conf:
            image = base_images["value"].split("/")
            registry = image[0] if len(image) > 1 else "docker.io"
            if registry in AUTHORIZED_REGISTRIES:
                return CheckResult.PASSED, None

        return CheckResult.FAILED, [base_images]


check = CheckBaseImage()
