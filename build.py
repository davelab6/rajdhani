#!/usr/bin/python

from subprocess import call
import os.path
import itfgfd

family_name = 'Rajdhani'

style_name_list = [
  'Light',
  'Regular',
  'Medium',
  'SemiBold',
  'Bold',
]

UFOInstanceGenerator_arg_list = [
  # '-kern',
  '-mark',
  # '-hint',
  '-flat',
  '-mkmk',
  '-clas',
  '-indi',
]

MakeOTF_arg_list = [
  '-r',
  '-shw',
]

match_mI_offset_dict = {
  'Light':    0,
  'Regular':  0,
  'Medium':   0,
  'SemiBold': 0,
  'Bold':     0,
}


print '\n#ITF: Resetting style directories...'
call(['rm', '-fr', 'styles'])
call(['mkdir', 'styles'])
for style_name in style_name_list:
  itfgfd.reset_style_dir(style_name)
  print '\tReset %s.' % style_name
print '#ITF: Done.\n'


call(
  [
    'UFOInstanceGenerator.py',
    'mm',
    '-o', 'styles',
  ] + UFOInstanceGenerator_arg_list
)


print '\n#ITF: Matching mI...'
for style_name in style_name_list:
  itfgfd.match_mI(
    style_name,
    stem_position_offset = match_mI_offset_dict[style_name],
  )
  print '\tMatched mI for %s.' % style_name
print '#ITF: Done.\n'


call(['rm', '-fr', 'build'])
call(['mkdir', 'build'])

for style_name in style_name_list:

  otf_path = 'build/%s-%s.otf' % (family_name, style_name)
  style_dir = 'styles/' + style_name

  call(
    [
      'makeotf',
      '-f', style_dir + '/font.ufo',
      '-o', otf_path,
      '-mf', 'FontMenuNameDB',
      '-gf', 'GlyphOrderAndAliasDB',
    ] + MakeOTF_arg_list
  )

  call(['rm', '-f', style_dir + '/current.fpr'])

  if os.path.exists(otf_path):
    call(['cp', '-f', otf_path, '/Library/Application Support/Adobe/Fonts'])
