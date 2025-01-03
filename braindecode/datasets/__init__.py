"""
Loader code for some datasets.
"""

from .base import WindowsDataset, BaseDataset, BaseConcatDataset
from .moabb import MOABBDataset, HGD, BNCI2014001
from .eegdash import EEGDashDataset
from .mne import create_from_mne_raw, create_from_mne_epochs
from .tuh import TUH, TUHAbnormal
from .sleep_physionet import SleepPhysionet
from .sleep_physio_challe_18 import SleepPhysionetChallenge2018
from .xy import create_from_X_y
from .bcicomp import BCICompetitionIVDataset4
from .nmt import NMT

__all__ = [
    "WindowsDataset",
    "BaseDataset",
    "BaseConcatDataset",
    "MOABBDataset",
    "EEGDashDataset",
    "HGD",
    "BNCI2014001",
    "create_from_mne_raw",
    "create_from_mne_epochs",
    "TUH",
    "TUHAbnormal",
    "NMT",
    "SleepPhysionet",
    "SleepPhysionetChallenge2018",
    "create_from_X_y",
    "BCICompetitionIVDataset4",
]
