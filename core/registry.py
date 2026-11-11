"""Catalogue of available sensor models — restricted to the Fabry-Perot interferometer."""
from __future__ import annotations

from . import glossary
from .base import SensorModel
from .optical import FabryPerotPressure

_ALL = [
    FabryPerotPressure(),
]

MODELS: dict[str, SensorModel] = {m.key: m for m in _ALL}

# every input gets a plain-language description (shown as the "?" tooltip in the sidebar)
for _m in _ALL:
    for _p in _m.params:
        if not _p.help:
            _p.help = glossary.param_help(_p.key, _p.label)

FAMILY_HELP = {
    "Optical": "The measurand shifts an optical interference fringe (intensity / phase).",
}


def families() -> list[str]:
    return list(FAMILY_HELP)


def subfamilies(family: str) -> list[str]:
    seen = []
    for m in _ALL:
        if m.family == family and m.subfamily not in seen:
            seen.append(m.subfamily)
    return seen


def models_of(family: str, subfamily: str | None = None) -> list[SensorModel]:
    return [m for m in _ALL if m.family == family and (subfamily is None or m.subfamily == subfamily)]


def get(key: str) -> SensorModel:
    return MODELS[key]
