
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSBIN DEC DIVIDE EQUALS FORMAT_BIN FORMAT_HEX HEX ID LPAREN MINUS PLUS RPAREN TIMESstatement : FORMAT_HEX expression\n    | FORMAT_BIN expressionstatement : ID EQUALS expressionstatement : expressionexpression : expression PLUS expression\n    | expression MINUS expression\n    | expression TIMES expression\n    | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENnumber : DEC \n    | HEX \n    | BINexpression : numberexpression : ID'
    
_lr_action_items = {'FORMAT_HEX':([0,],[2,]),'FORMAT_BIN':([0,],[4,]),'ID':([0,2,4,6,7,14,15,16,17,19,],[5,13,13,13,13,13,13,13,13,13,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[6,6,15,6,-15,6,6,-14,-11,-12,-13,15,-15,6,6,6,6,15,6,-9,15,-5,-6,-7,-8,15,-10,]),'LPAREN':([0,2,4,6,7,14,15,16,17,19,],[7,7,7,7,7,7,7,7,7,7,]),'DEC':([0,2,4,6,7,14,15,16,17,19,],[9,9,9,9,9,9,9,9,9,9,]),'HEX':([0,2,4,6,7,14,15,16,17,19,],[10,10,10,10,10,10,10,10,10,10,]),'BIN':([0,2,4,6,7,14,15,16,17,19,],[11,11,11,11,11,11,11,11,11,11,]),'$end':([1,3,5,8,9,10,11,12,13,18,20,22,23,24,25,26,27,],[0,-4,-15,-14,-11,-12,-13,-1,-15,-2,-9,-5,-6,-7,-8,-3,-10,]),'PLUS':([3,5,8,9,10,11,12,13,18,20,21,22,23,24,25,26,27,],[14,-15,-14,-11,-12,-13,14,-15,14,-9,14,-5,-6,-7,-8,14,-10,]),'TIMES':([3,5,8,9,10,11,12,13,18,20,21,22,23,24,25,26,27,],[16,-15,-14,-11,-12,-13,16,-15,16,-9,16,16,16,-7,-8,16,-10,]),'DIVIDE':([3,5,8,9,10,11,12,13,18,20,21,22,23,24,25,26,27,],[17,-15,-14,-11,-12,-13,17,-15,17,-9,17,17,17,-7,-8,17,-10,]),'EQUALS':([5,],[19,]),'RPAREN':([8,9,10,11,13,20,21,22,23,24,25,27,],[-14,-11,-12,-13,-15,-9,27,-5,-6,-7,-8,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,2,4,6,7,14,15,16,17,19,],[3,12,18,20,21,22,23,24,25,26,]),'number':([0,2,4,6,7,14,15,16,17,19,],[8,8,8,8,8,8,8,8,8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> FORMAT_HEX expression','statement',2,'p_statement_format','commandline-calc.py',86),
  ('statement -> FORMAT_BIN expression','statement',2,'p_statement_format','commandline-calc.py',87),
  ('statement -> ID EQUALS expression','statement',3,'p_statement_assign','commandline-calc.py',92),
  ('statement -> expression','statement',1,'p_statement_expr','commandline-calc.py',97),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','commandline-calc.py',101),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','commandline-calc.py',102),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','commandline-calc.py',103),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','commandline-calc.py',104),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','commandline-calc.py',111),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','commandline-calc.py',115),
  ('number -> DEC','number',1,'p_number','commandline-calc.py',119),
  ('number -> HEX','number',1,'p_number','commandline-calc.py',120),
  ('number -> BIN','number',1,'p_number','commandline-calc.py',121),
  ('expression -> number','expression',1,'p_expression_number','commandline-calc.py',125),
  ('expression -> ID','expression',1,'p_expression_name','commandline-calc.py',129),
]
