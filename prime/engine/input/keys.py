from PyQt5.QtCore import Qt


class BaseKeys:
    """
    Namespace for mapping key constants.
    This is simply a template for what keys should be mapped for all window libraries
    """
    # Fallback press/release action when window libraries don't have this
    ACTION_PRESS = 'ACTION_PRESS'
    ACTION_RELEASE = 'ACTION_RELEASE'

    ESCAPE = None
    SPACE = None
    ENTER = None
    PAGE_UP = None
    PAGE_DOWN = None
    LEFT = None
    RIGHT = None
    UP = None
    DOWN = None

    A = None
    B = None
    C = None
    D = None
    E = None
    F = None
    G = None
    H = None
    I = None
    J = None
    K = None
    L = None
    M = None
    N = None
    O = None
    P = None
    Q = None
    R = None
    S = None
    T = None
    U = None
    V = None
    W = None
    X = None
    Y = None
    Z = None


class Keys(BaseKeys):
    """
    Namespace mapping pyqt specific key constants
    """
    ESCAPE = Qt.Key_Escape
    SPACE = Qt.Key_Space
    ENTER = Qt.Key_Enter
    PAGE_UP = Qt.Key_PageUp
    PAGE_DOWN = Qt.Key_PageDown
    LEFT = Qt.Key_Left
    RIGHT = Qt.Key_Right
    UP = Qt.Key_Up
    DOWN = Qt.Key_Down

    A = Qt.Key_A
    B = Qt.Key_B
    C = Qt.Key_C
    D = Qt.Key_D
    E = Qt.Key_E
    F = Qt.Key_F
    G = Qt.Key_G
    H = Qt.Key_H
    I = Qt.Key_I
    J = Qt.Key_J
    K = Qt.Key_K
    L = Qt.Key_L
    M = Qt.Key_M
    N = Qt.Key_N
    O = Qt.Key_O
    P = Qt.Key_P
    Q = Qt.Key_Q
    R = Qt.Key_R
    S = Qt.Key_S
    T = Qt.Key_T
    U = Qt.Key_U
    V = Qt.Key_V
    W = Qt.Key_W
    X = Qt.Key_X
    Y = Qt.Key_Y
    Z = Qt.Key_Z
