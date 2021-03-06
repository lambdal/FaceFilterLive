from localization import L
from xlib import qt as qtx

from ..backend import FaceModifier
from .widgets.QBackendPanel import QBackendPanel
from .widgets.QLabelPopupInfo import QLabelPopupInfo
from .widgets.QSliderCSWNumber import QSliderCSWNumber


class QFaceModifier(QBackendPanel):
    def __init__(self, backend : FaceModifier):
        cs = backend.get_control_sheet()

        q_beard_label = QLabelPopupInfo(label="beard", popup_info_text="")
        q_beard = QSliderCSWNumber(cs.goatee, reflect_state_widgets=[q_beard_label])

        q_smile_label = QLabelPopupInfo(label="smile", popup_info_text="")
        q_smile = QSliderCSWNumber(cs.smile, reflect_state_widgets=[q_smile_label])

        q_age_label = QLabelPopupInfo(label="age", popup_info_text="")
        q_age = QSliderCSWNumber(cs.age, reflect_state_widgets=[q_age_label])

        grid_l = qtx.QXGridLayout(spacing=5)
        row = 0
        grid_l.addWidget(q_beard_label, row, 0, alignment=qtx.AlignRight | qtx.AlignVCenter  )
        grid_l.addWidget(q_beard, row, 1, alignment=qtx.AlignLeft )
        row += 1
        grid_l.addWidget(q_smile_label, row, 0, alignment=qtx.AlignRight | qtx.AlignVCenter  )
        grid_l.addWidget(q_smile, row, 1, alignment=qtx.AlignLeft )
        row +=1 
        grid_l.addWidget(q_age_label, row, 0, alignment=qtx.AlignRight | qtx.AlignVCenter  )
        grid_l.addWidget(q_age, row, 1, alignment=qtx.AlignLeft )

        super().__init__(backend, "modifier",
                         layout=qtx.QXVBoxLayout([grid_l]))

