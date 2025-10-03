from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ._models.storage import StoragePolicyConfig
from .storage_policies import WandbStoragePolicy

if TYPE_CHECKING:
    from .storage_policy import StoragePolicy


def make_storage_policy(**kwargs: Any) -> StoragePolicy:
    """A factory function that returns the default StoragePolicy for the current environment."""
    config = StoragePolicyConfig.from_env(**kwargs)
    return WandbStoragePolicy.from_config(config)
