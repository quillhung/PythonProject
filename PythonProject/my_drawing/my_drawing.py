"""
File: my_drawing
Name: Quill
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    title: One of the most famous paintings in the world.

    stanCode is dedicated to programming education
    and has now created a gallery that combines programming and art,
    with Karel as the CEO.
    The first artwork on display is one of the most famous paintings in the world,
    'Girl with a Pearl Earring - Johannes Vermeer, 1665'.
    """
    # window size
    window = GWindow(width=500, height=500, title='One of the most famous paintings in the world')
    # draw karel
    karel_body = GRect(25, 30, x=100, y=450)
    karel_body.filled = True
    karel_body.fill_color = 'darkblue'
    window.add(karel_body)
    hand_r = GRect(15, 5, x=105, y=445)
    hand_r.filled = True
    hand_r.fill_color = 'green'
    window.add(hand_r)
    hand_l = GRect(15, 5, x=105, y=480)
    hand_l.filled = True
    hand_l.fill_color = 'green'
    window.add(hand_l)
    head = GOval(18, 28, x=125, y=450)
    head.filled = True
    head.fill_color = 'grey'
    window.add(head)
    feet_r = GOval(8, 10, x=92, y=452)
    feet_r.filled = True
    feet_r.fill_color = 'orangered'
    window.add(feet_r)
    feet_l = GOval(8, 10, x=92, y=468)
    feet_l.filled = True
    feet_l.fill_color = 'orangered'
    window.add(feet_l)
    eye_l = GRect(5, 5, x=132, y=456)
    eye_l.filled = True
    eye_l.fill_color = 'darkblue'
    window.add(eye_l)
    eye_l = GRect(5, 5, x=132, y=466)
    eye_l.filled = True
    eye_l.fill_color = 'darkblue'
    window.add(eye_l)
    # draw K
    k = GRect(21, 2, x=102, y=456)
    k.filled = True
    k.color = 'white'
    k.fill_color = 'white'
    window.add(k)
    k = GRect(3, 3, x=111, y=459)
    k.filled = True
    k.color = 'white'
    k.fill_color = 'white'
    window.add(k)
    k = GRect(3, 3, x=108, y=462)
    k.filled = True
    k.color = 'white'
    k.fill_color = 'white'
    window.add(k)
    k = GRect(3, 3, x=114, y=462)
    k.filled = True
    k.color = 'white'
    k.fill_color = 'white'
    window.add(k)
    k = GRect(3, 3, x=105, y=465)
    k.filled = True
    k.color = 'white'
    k.fill_color = 'white'
    window.add(k)
    k = GRect(3, 3, x=117, y=465)
    k.filled = True
    k.color = 'white'
    k.fill_color = 'white'
    window.add(k)
    k = GRect(3, 3, x=102, y=468)
    k.filled = True
    k.color = 'white'
    k.fill_color = 'white'
    window.add(k)
    k = GRect(3, 3, x=120, y=468)
    k.filled = True
    k.color = 'white'
    k.fill_color = 'white'
    window.add(k)

    # label
    label = GLabel('Girl with a Pearl Earring - Johannes Vermeer')
    label.font = 'Verdana-15-bold-italic'
    window.add(label, x=60, y=label.height+10)
    stancode = GLabel('stanCode Gallery')
    stancode.font = 'Verdana-15-bold-italic'
    window.add(stancode, x=170, y=500-stancode.height)

    # frame
    frame = GOval(200, 300, x=120, y=80)
    frame.filled = True
    frame.color = 'palevioletred'
    frame.fill_color = 'palevioletred'
    window.add(frame)

    # draw black line
    # layer 1
    line = GRect(10, 10, x=260, y=90)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=270, y=90)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=280, y=90)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=290, y=90)
    line.filled = True
    window.add(line)
    # layer 2
    line = GRect(10, 10, x=250, y=100)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=300, y=100)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=100)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=100)
    line.filled = True
    window.add(line)
    # layer 3
    line = GRect(10, 10, x=220, y=110)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=230, y=110)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=240, y=110)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=250, y=110)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=260, y=110)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=270, y=110)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=110)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=330, y=110)
    line.filled = True
    window.add(line)
    # layer 4
    line = GRect(10, 10, x=210, y=120)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=280, y=120)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=290, y=120)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=120)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=120)
    line.filled = True
    window.add(line)
    # layer 5
    line = GRect(10, 10, x=200, y=130)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=300, y=130)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=130)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=130)
    line.filled = True
    window.add(line)
    # layer 6
    line = GRect(10, 10, x=200, y=140)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=210, y=140)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=220, y=140)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=230, y=140)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=240, y=140)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=140)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=140)
    line.filled = True
    window.add(line)
    # layer 7
    line = GRect(10, 10, x=190, y=150)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=250, y=150)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=260, y=150)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=150)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=350, y=150)
    line.filled = True
    window.add(line)
    # layer 8
    line = GRect(10, 10, x=190, y=160)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=270, y=160)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=160)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=350, y=160)
    line.filled = True
    window.add(line)
    # layer 9
    line = GRect(10, 10, x=190, y=170)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=280, y=170)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=170)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=350, y=170)
    line.filled = True
    window.add(line)
    # layer 10
    line = GRect(10, 10, x=190, y=180)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=280, y=180)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=180)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=350, y=180)
    line.filled = True
    window.add(line)
    # layer 11
    line = GRect(10, 10, x=190, y=190)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=280, y=190)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=290, y=190)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=190)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=360, y=190)
    line.filled = True
    window.add(line)
    # layer 12
    line = GRect(10, 10, x=190, y=200)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=300, y=200)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=200)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=360, y=200)
    line.filled = True
    window.add(line)
    # layer 13
    line = GRect(10, 10, x=190, y=210)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=300, y=210)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=210)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=360, y=210)
    line.filled = True
    window.add(line)
    # layer 14
    line = GRect(10, 10, x=190, y=220)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=280, y=220)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=290, y=220)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=220)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=360, y=220)
    line.filled = True
    window.add(line)
    # layer 15 (on mouth)
    line = GRect(10, 10, x=190, y=230)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=270, y=230)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=300, y=230)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=230)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=360, y=230)
    line.filled = True
    window.add(line)
    # layer 16
    line = GRect(10, 10, x=200, y=240)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=250, y=240)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=260, y=240)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=270, y=240)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=300, y=240)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=240)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=360, y=240)
    line.filled = True
    window.add(line)
    # layer 17
    line = GRect(10, 10, x=210, y=250)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=220, y=250)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=230, y=250)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=240, y=250)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=280, y=250)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=290, y=250)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=250)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=360, y=250)
    line.filled = True
    window.add(line)
    # layer 18
    line = GRect(10, 10, x=240, y=260)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=260, y=260)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=270, y=260)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=260)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=260)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=360, y=260)
    line.filled = True
    window.add(line)
    # layer 19
    line = GRect(10, 10, x=240, y=270)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=250, y=270)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=270)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=270)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=360, y=270)
    line.filled = True
    window.add(line)
    # layer 20
    line = GRect(10, 10, x=230, y=280)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=270, y=280)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=280, y=280)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=290, y=280)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=300, y=280)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=280)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=280)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=360, y=280)
    line.filled = True
    window.add(line)
    # layer 21
    line = GRect(10, 10, x=220, y=290)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=250, y=290)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=260, y=290)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=290)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=290)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=350, y=290)
    line.filled = True
    window.add(line)
    # layer 22
    line = GRect(10, 10, x=220, y=300)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=240, y=300)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=300)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=300)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=330, y=300)
    line.filled = True
    window.add(line)
    # layer 23
    line = GRect(10, 10, x=210, y=310)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=230, y=310)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=310)
    line.filled = True
    window.add(line)
    # layer 24
    line = GRect(10, 10, x=210, y=320)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=230, y=320)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=320)
    line.filled = True
    window.add(line)
    # layer 25
    line = GRect(10, 10, x=200, y=330)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=220, y=330)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=330)
    line.filled = True
    window.add(line)
    # layer 26 (the last row)
    line = GRect(10, 10, x=200, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=210, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=220, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=230, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=240, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=250, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=260, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=270, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=280, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=290, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=300, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=310, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=320, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=330, y=340)
    line.filled = True
    window.add(line)
    line = GRect(10, 10, x=340, y=340)
    line.filled = True
    window.add(line)

    # draw face shadow
    face_shadow = GRect(10, 10, x=200, y=150)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=210, y=150)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=220, y=150)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=230, y=150)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=240, y=150)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=250, y=160)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=260, y=160)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=270, y=170)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=270, y=180)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=270, y=190)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=280, y=200)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=280, y=210)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=290, y=200)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=290, y=210)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=270, y=220)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=260, y=230)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=240, y=240)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=210, y=240)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=200, y=230)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=200, y=190)
    face_shadow.filled = True
    face_shadow.color = 'papayawhip'
    face_shadow.fill_color = 'papayawhip'
    window.add(face_shadow)
    # draw neck
    face_shadow = GRect(10, 10, x=250, y=250)
    face_shadow.filled = True
    face_shadow.color = 'oldlace'
    face_shadow.fill_color = 'oldlace'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=260, y=250)
    face_shadow.filled = True
    face_shadow.color = 'peachpuff'
    face_shadow.fill_color = 'peachpuff'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=270, y=250)
    face_shadow.filled = True
    face_shadow.color = 'peachpuff'
    face_shadow.fill_color = 'peachpuff'
    window.add(face_shadow)
    face_shadow = GRect(10, 10, x=250, y=260)
    face_shadow.filled = True
    face_shadow.color = 'peachpuff'
    face_shadow.fill_color = 'peachpuff'
    window.add(face_shadow)

    # draw face
    face = GRect(10, 10, x=200, y=160)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=210, y=160)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=220, y=160)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=230, y=160)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=240, y=160)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=200, y=170)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=210, y=170)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=220, y=170)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=230, y=170)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=240, y=170)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=250, y=170)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=260, y=170)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=200, y=180)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=210, y=180)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=220, y=180)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=230, y=180)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=240, y=180)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=250, y=180)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=260, y=180)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=220, y=190)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=230, y=190)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=240, y=190)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=260, y=190)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=200, y=200)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=220, y=200)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=230, y=200)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=240, y=200)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=260, y=200)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=270, y=200)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=210, y=210)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=230, y=210)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=240, y=210)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=270, y=210)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=200, y=220)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=210, y=220)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=220, y=220)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=230, y=220)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=240, y=220)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=250, y=220)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=260, y=220)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=210, y=230)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=240, y=230)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=250, y=230)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=220, y=240)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    face = GRect(10, 10, x=230, y=240)
    face.filled = True
    face.color = 'oldlace'
    face.fill_color = 'oldlace'
    window.add(face)
    # draw mouth
    mouth = GRect(10, 10, x=220, y=230)
    mouth.filled = True
    window.add(mouth)
    mouth = GRect(10, 10, x=230, y=230)
    mouth.filled = True
    window.add(mouth)
    # draw nose
    nose = GRect(10, 10, x=220, y=210)
    nose.filled = True
    window.add(nose)
    # draw eyes
    # left eye
    eye_l = GRect(10, 10, x=200, y=180)
    eye_l.filled = True
    window.add(eye_l)
    eye_l = GRect(10, 10, x=210, y=190)
    eye_l.filled = True
    window.add(eye_l)
    eye_l = GRect(10, 10, x=210, y=200)
    eye_l.filled = True
    window.add(eye_l)
    # right eye
    eye_r = GRect(10, 10, x=240, y=180)
    eye_r.filled = True
    window.add(eye_r)
    eye_r = GRect(10, 10, x=250, y=190)
    eye_r.filled = True
    window.add(eye_r)
    eye_r = GRect(10, 10, x=250, y=200)
    eye_r.filled = True
    window.add(eye_r)
    # draw face pink
    face_pink = GRect(10, 10, x=250, y=210)
    face_pink.filled = True
    face_pink.color = 'lightpink'
    face_pink.fill_color = 'lightpink'
    window.add(face_pink)
    face_pink = GRect(10, 10, x=260, y=210)
    face_pink.filled = True
    face_pink.color = 'lightpink'
    face_pink.fill_color = 'lightpink'
    window.add(face_pink)
    face_pink = GRect(10, 10, x=200, y=210)
    face_pink.filled = True
    face_pink.color = 'lightpink'
    face_pink.fill_color = 'lightpink'
    window.add(face_pink)

    # draw scarf
    # layer 1
    scarf = GRect(10, 10, x=260, y=100)
    scarf.filled = True
    scarf.color = 'darkgoldenrod'
    scarf.fill_color = 'darkgoldenrod'
    window.add(scarf)
    scarf = GRect(10, 10, x=270, y=100)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=280, y=100)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=290, y=100)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    # layer 2
    scarf = GRect(10, 10, x=280, y=110)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=290, y=110)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=300, y=110)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=320, y=110)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    # layer 3
    scarf = GRect(10, 10, x=300, y=120)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=310, y=120)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=120)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    # layer 4
    scarf = GRect(10, 10, x=310, y=130)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=130)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    # layer 5
    scarf = GRect(10, 10, x=320, y=140)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=140)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    # layer 6
    scarf = GRect(10, 10, x=320, y=150)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=150)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=150)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    # layer 7
    scarf = GRect(10, 10, x=330, y=160)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=160)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    # layer 8
    scarf = GRect(10, 10, x=330, y=170)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=170)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    # layer 9
    scarf = GRect(10, 10, x=330, y=180)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=180)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    # layer 10
    scarf = GRect(10, 10, x=330, y=190)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=190)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=350, y=190)
    scarf.filled = True
    scarf.color = 'darkgoldenrod'
    scarf.fill_color = 'darkgoldenrod'
    window.add(scarf)
    # layer 11
    scarf = GRect(10, 10, x=330, y=200)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=200)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=350, y=200)
    scarf.filled = True
    scarf.color = 'darkgoldenrod'
    scarf.fill_color = 'darkgoldenrod'
    window.add(scarf)
    # layer 12
    scarf = GRect(10, 10, x=330, y=210)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=210)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=350, y=210)
    scarf.filled = True
    scarf.color = 'darkgoldenrod'
    scarf.fill_color = 'darkgoldenrod'
    window.add(scarf)
    # layer 13
    scarf = GRect(10, 10, x=320, y=220)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=220)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=220)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=350, y=220)
    scarf.filled = True
    scarf.color = 'darkgoldenrod'
    scarf.fill_color = 'darkgoldenrod'
    window.add(scarf)
    # layer 14
    scarf = GRect(10, 10, x=320, y=230)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=230)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=230)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=350, y=230)
    scarf.filled = True
    scarf.color = 'darkgoldenrod'
    scarf.fill_color = 'darkgoldenrod'
    window.add(scarf)
    # layer 15
    scarf = GRect(10, 10, x=320, y=240)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=240)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=240)
    scarf.filled = True
    scarf.color = 'darkgoldenrod'
    scarf.fill_color = 'darkgoldenrod'
    window.add(scarf)
    scarf = GRect(10, 10, x=350, y=240)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    # layer 16
    scarf = GRect(10, 10, x=320, y=250)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=250)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=340, y=250)
    scarf.filled = True
    scarf.color = 'darkgoldenrod'
    scarf.fill_color = 'darkgoldenrod'
    window.add(scarf)
    scarf = GRect(10, 10, x=350, y=250)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    # layer 17
    scarf = GRect(10, 10, x=320, y=260)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=260)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=350, y=260)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    # layer 18
    scarf = GRect(10, 10, x=320, y=270)
    scarf.filled = True
    scarf.color = 'lightgoldenrodyellow'
    scarf.fill_color = 'lightgoldenrodyellow'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=270)
    scarf.filled = True
    scarf.color = 'gold'
    scarf.fill_color = 'gold'
    window.add(scarf)
    scarf = GRect(10, 10, x=350, y=270)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    # layer 19
    scarf = GRect(10, 10, x=320, y=280)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=280)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=350, y=280)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 20
    scarf = GRect(10, 10, x=320, y=290)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=330, y=290)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)

    # draw head scarf
    # layer 1
    scarf = GRect(10, 10, x=220, y=120)
    scarf.filled = True
    scarf.color = 'powderblue'
    scarf.fill_color = 'powderblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=230, y=120)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=240, y=120)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=250, y=120)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=260, y=120)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=270, y=120)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 2
    scarf = GRect(10, 10, x=210, y=130)
    scarf.filled = True
    scarf.color = 'powderblue'
    scarf.fill_color = 'powderblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=220, y=130)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=230, y=130)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=240, y=130)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=250, y=130)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=260, y=130)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=270, y=130)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=280, y=130)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=290, y=130)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 3
    scarf = GRect(10, 10, x=250, y=140)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=260, y=140)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=270, y=140)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=280, y=140)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=290, y=140)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=300, y=140)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 4
    scarf = GRect(10, 10, x=270, y=150)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=280, y=150)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=290, y=150)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=300, y=150)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 5
    scarf = GRect(10, 10, x=280, y=160)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=290, y=160)
    scarf.filled = True
    scarf.color = 'royalblue'
    scarf.fill_color = 'royalblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=300, y=160)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=310, y=160)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 6
    scarf = GRect(10, 10, x=290, y=170)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=300, y=170)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=310, y=170)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 7
    scarf = GRect(10, 10, x=290, y=180)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=300, y=180)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=310, y=180)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 8
    scarf = GRect(10, 10, x=300, y=190)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    scarf = GRect(10, 10, x=310, y=190)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 9
    scarf = GRect(10, 10, x=310, y=200)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 10
    scarf = GRect(10, 10, x=310, y=210)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # layer 11
    scarf = GRect(10, 10, x=300, y=220)
    scarf.filled = True
    scarf.color = 'darkblue'
    scarf.fill_color = 'darkblue'
    window.add(scarf)
    # draw pearl earring
    pearl = GRect(10, 10, x=280, y=230)
    pearl.filled = True
    pearl.color = 'white'
    pearl.fill_color = 'white'
    window.add(pearl)
    pearl = GRect(10, 10, x=290, y=230)
    pearl.filled = True
    pearl.color = 'silver'
    pearl.fill_color = 'silver'
    window.add(pearl)
    pearl = GRect(10, 10, x=280, y=240)
    pearl.filled = True
    pearl.color = 'silver'
    pearl.fill_color = 'silver'
    window.add(pearl)
    pearl = GRect(10, 10, x=290, y=240)
    pearl.filled = True
    pearl.color = 'dimgray'
    pearl.fill_color = 'dimgray'
    window.add(pearl)
    # draw clothing
    # layer 1
    clothing = GRect(10, 10, x=300, y=250)
    clothing.filled = True
    clothing.color = 'ivory'
    clothing.fill_color = 'ivory'
    window.add(clothing)
    # layer 2
    clothing = GRect(10, 10, x=280, y=260)
    clothing.filled = True
    clothing.color = 'ivory'
    clothing.fill_color = 'ivory'
    window.add(clothing)
    clothing = GRect(10, 10, x=290, y=260)
    clothing.filled = True
    clothing.color = 'ivory'
    clothing.fill_color = 'ivory'
    window.add(clothing)
    clothing = GRect(10, 10, x=300, y=260)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    # layer 3
    clothing = GRect(10, 10, x=260, y=270)
    clothing.filled = True
    clothing.color = 'ivory'
    clothing.fill_color = 'ivory'
    window.add(clothing)
    clothing = GRect(10, 10, x=270, y=270)
    clothing.filled = True
    clothing.color = 'ivory'
    clothing.fill_color = 'ivory'
    window.add(clothing)
    clothing = GRect(10, 10, x=280, y=270)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=290, y=270)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=300, y=270)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    # layer 4
    clothing = GRect(10, 10, x=240, y=280)
    clothing.filled = True
    clothing.color = 'ivory'
    clothing.fill_color = 'ivory'
    window.add(clothing)
    clothing = GRect(10, 10, x=250, y=280)
    clothing.filled = True
    clothing.color = 'ivory'
    clothing.fill_color = 'ivory'
    window.add(clothing)
    clothing = GRect(10, 10, x=260, y=280)
    clothing.filled = True
    clothing.color = 'cornsilk'
    clothing.fill_color = 'cornsilk'
    window.add(clothing)
    # layer 5
    clothing = GRect(10, 10, x=230, y=290)
    clothing.filled = True
    clothing.color = 'ivory'
    clothing.fill_color = 'ivory'
    window.add(clothing)
    clothing = GRect(10, 10, x=240, y=290)
    clothing.filled = True
    clothing.color = 'cornsilk'
    clothing.fill_color = 'cornsilk'
    window.add(clothing)
    clothing = GRect(10, 10, x=270, y=290)
    clothing.filled = True
    clothing.color = 'cornsilk'
    clothing.fill_color = 'cornsilk'
    window.add(clothing)
    clothing = GRect(10, 10, x=280, y=290)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=290, y=290)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=300, y=290)
    clothing.filled = True
    clothing.color = 'darkgoldenrod'
    clothing.fill_color = 'darkgoldenrod'
    window.add(clothing)
    # layer 6
    clothing = GRect(10, 10, x=230, y=300)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=250, y=300)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=260, y=300)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=270, y=300)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=280, y=300)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=290, y=300)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=300, y=300)
    clothing.filled = True
    clothing.color = 'darkgoldenrod'
    clothing.fill_color = 'darkgoldenrod'
    window.add(clothing)
    # layer 7
    clothing = GRect(10, 10, x=220, y=310)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=240, y=310)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=250, y=310)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=260, y=310)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=270, y=310)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=280, y=310)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=290, y=310)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=300, y=310)
    clothing.filled = True
    clothing.color = 'darkgoldenrod'
    clothing.fill_color = 'darkgoldenrod'
    window.add(clothing)
    clothing = GRect(10, 10, x=310, y=310)
    clothing.filled = True
    clothing.color = 'darkgoldenrod'
    clothing.fill_color = 'darkgoldenrod'
    window.add(clothing)
    clothing = GRect(10, 10, x=320, y=310)
    clothing.filled = True
    clothing.color = 'darkgoldenrod'
    clothing.fill_color = 'darkgoldenrod'
    window.add(clothing)
    clothing = GRect(10, 10, x=330, y=310)
    clothing.filled = True
    clothing.color = 'darkgoldenrod'
    clothing.fill_color = 'darkgoldenrod'
    window.add(clothing)
    # layer 8
    clothing = GRect(10, 10, x=220, y=320)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=240, y=320)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=250, y=320)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=260, y=320)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=270, y=320)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=280, y=320)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=290, y=320)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=300, y=320)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=310, y=320)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=320, y=320)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=330, y=320)
    clothing.filled = True
    clothing.color = 'darkgoldenrod'
    clothing.fill_color = 'darkgoldenrod'
    window.add(clothing)
    # layer 9
    clothing = GRect(10, 10, x=210, y=330)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=230, y=330)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=240, y=330)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=250, y=330)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=260, y=330)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=270, y=330)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=280, y=330)
    clothing.filled = True
    clothing.color = 'lightgoldenrodyellow'
    clothing.fill_color = 'lightgoldenrodyellow'
    window.add(clothing)
    clothing = GRect(10, 10, x=290, y=330)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=300, y=330)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=310, y=330)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=320, y=330)
    clothing.filled = True
    clothing.color = 'gold'
    clothing.fill_color = 'gold'
    window.add(clothing)
    clothing = GRect(10, 10, x=330, y=330)
    clothing.filled = True
    clothing.color = 'darkgoldenrod'
    clothing.fill_color = 'darkgoldenrod'
    window.add(clothing)


if __name__ == '__main__':
    main()
