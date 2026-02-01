#
# P l o t . p y
#

# TODO:  This doesn't work because of comparisons between floats and integers.
def BwRev(oldColor):
  revStr = {'w': 'b', 'b': 'w', 'white': 'black', 'black': 'white'}
  revRgb = {(0,0,0): (1,1,1), (1,1,1): (0,0,0)}

  if type(oldColor) == str:
    if oldColor in revStr:
      return revStr[oldColor]

  elif type(oldColor) == tuple:
    oldRgb = oldColor[:3]
    if oldRgb in revRgb:
      newRgb = revRgb[oldRgb]

      if len(oldColor) == 4:
        return newRgb + oldColor[3]
      elif len(oldColor) == 3:
        return newRgb

  return oldColor

# TODO:  This works, but for all the wrong reasons.  Was in a hurry ... basically didn't finish.
def SaveBwRev(fig,ax, fileName):
  xLabel = ax.get_xlabel()
  if xLabel != '':
    oldColor = ax.xaxis.label.get_color()
    newColor = BwRev(oldColor)
    if oldColor != newColor:
      ax.xaxis.label.set_color(newColor)

  yLabel = ax.get_xlabel()
  if yLabel != '':
    oldColor = ax.yaxis.label.get_color()
    newColor = BwRev(oldColor)
    if oldColor != newColor:
      ax.yaxis.label.set_color(newColor)

  title = ax.get_title()
  if title != '':
    oldColor = ax.title.get_color()
    newColor = BwRev(oldColor)
    if oldColor != newColor:
      ax.title.set_color(newColor)

  # TODO: emergency first aid, because there is not get_color methods
  # ax.xaxis.label.set_color('black')
  # ax.yaxis.label.set_color('black')
  # ax.title.set_color('black')

  for s in ax.spines.values():
    s.set_color('black')

  ax.tick_params(axis='both', colors='black')

  # faceColor = ax.get_facecolor()
  # newFaceColor = BwRev(faceColor)
  # if faceColor != newFaceColor:
  #   ax.set_facecolor(newFaceColor)

  ax.set_facecolor('white')
  fig.set_facecolor('white')

  for line in ax.get_lines():
    color = line.get_color()
    newColor = BwRev(color)
    if color != newColor:
      line.set_color(newColor)

  ax.legend(labelcolor='black', facecolor='white')

  ax.figure.savefig(fileName)
