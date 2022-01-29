# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sat_descrip.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11sat_descrip.proto\x12\x07LEOHack\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"-\n\x06Pose2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05theta\x18\x03 \x01(\x02\"2\n\x07Twist2D\x12\x0b\n\x03v_x\x18\x01 \x01(\x02\x12\x0b\n\x03v_y\x18\x02 \x01(\x02\x12\r\n\x05omega\x18\x03 \x01(\x02\"1\n\x08Wrench2D\x12\x0b\n\x03\x66_x\x18\x01 \x01(\x02\x12\x0b\n\x03\x66_y\x18\x02 \x01(\x02\x12\x0b\n\x03tau\x18\x03 \x01(\x02\",\n\x08TeamInfo\x12\x10\n\x08teamName\x18\x01 \x01(\t\x12\x0e\n\x06teamID\x18\x02 \x01(\r\"m\n\x14SatelliteDescription\x12#\n\x08teamInfo\x18\x01 \x01(\x0b\x32\x11.LEOHack.TeamInfo\x12\x0c\n\x04mass\x18\x02 \x01(\x02\x12\x0f\n\x07inertia\x18\x03 \x01(\x02\x12\x11\n\tipAddress\x18\x05 \x01(\t\"}\n\rSataliteState\x12\x0e\n\x06teamID\x18\x01 \x01(\r\x12\x0e\n\x06\x61\x63tive\x18\x02 \x01(\x08\x12\x1d\n\x04pose\x18\x03 \x01(\x0b\x32\x0f.LEOHack.Pose2D\x12\x1f\n\x05twist\x18\x04 \x01(\x0b\x32\x10.LEOHack.Twist2D\x12\x0c\n\x04\x66uel\x18\x05 \x01(\x02\"\xcc\x01\n\x0bSystemState\x12)\n\x05state\x18\x01 \x01(\x0e\x32\x1a.LEOHack.SystemState.State\x12.\n\x0b\x65lapsedTime\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x30\n\x0c\x61\x62soluteTime\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"0\n\x05State\x12\x08\n\x04INIT\x10\x00\x12\x07\n\x03RUN\x10\x01\x12\t\n\x05RESET\x10\x02\x12\t\n\x05\x41\x42ORT\x10\x03\"\x85\x01\n\x07\x43ommand\x12-\n\x0b\x63ommandType\x18\x01 \x01(\x0e\x32\x18.LEOHack.Command.CmdType\"K\n\x07\x43mdType\x12\x08\n\x04INIT\x10\x00\x12\t\n\x05START\x10\x01\x12\t\n\x05PAUSE\x10\x02\x12\t\n\x05\x41\x42ORT\x10\x03\x12\t\n\x05RESET\x10\x04\x12\n\n\x06REBOOT\x10\x05\"2\n\rThrustCommand\x12!\n\x06thrust\x18\x01 \x01(\x0b\x32\x11.LEOHack.Wrench2D\"\x1f\n\x0c\x43ommandReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x62\x06proto3')



_POSE2D = DESCRIPTOR.message_types_by_name['Pose2D']
_TWIST2D = DESCRIPTOR.message_types_by_name['Twist2D']
_WRENCH2D = DESCRIPTOR.message_types_by_name['Wrench2D']
_TEAMINFO = DESCRIPTOR.message_types_by_name['TeamInfo']
_SATELLITEDESCRIPTION = DESCRIPTOR.message_types_by_name['SatelliteDescription']
_SATALITESTATE = DESCRIPTOR.message_types_by_name['SataliteState']
_SYSTEMSTATE = DESCRIPTOR.message_types_by_name['SystemState']
_COMMAND = DESCRIPTOR.message_types_by_name['Command']
_THRUSTCOMMAND = DESCRIPTOR.message_types_by_name['ThrustCommand']
_COMMANDREPLY = DESCRIPTOR.message_types_by_name['CommandReply']
_SYSTEMSTATE_STATE = _SYSTEMSTATE.enum_types_by_name['State']
_COMMAND_CMDTYPE = _COMMAND.enum_types_by_name['CmdType']
Pose2D = _reflection.GeneratedProtocolMessageType('Pose2D', (_message.Message,), {
  'DESCRIPTOR' : _POSE2D,
  '__module__' : 'sat_descrip_pb2'
  # @@protoc_insertion_point(class_scope:LEOHack.Pose2D)
  })
_sym_db.RegisterMessage(Pose2D)

Twist2D = _reflection.GeneratedProtocolMessageType('Twist2D', (_message.Message,), {
  'DESCRIPTOR' : _TWIST2D,
  '__module__' : 'sat_descrip_pb2'
  # @@protoc_insertion_point(class_scope:LEOHack.Twist2D)
  })
_sym_db.RegisterMessage(Twist2D)

Wrench2D = _reflection.GeneratedProtocolMessageType('Wrench2D', (_message.Message,), {
  'DESCRIPTOR' : _WRENCH2D,
  '__module__' : 'sat_descrip_pb2'
  # @@protoc_insertion_point(class_scope:LEOHack.Wrench2D)
  })
_sym_db.RegisterMessage(Wrench2D)

TeamInfo = _reflection.GeneratedProtocolMessageType('TeamInfo', (_message.Message,), {
  'DESCRIPTOR' : _TEAMINFO,
  '__module__' : 'sat_descrip_pb2'
  # @@protoc_insertion_point(class_scope:LEOHack.TeamInfo)
  })
_sym_db.RegisterMessage(TeamInfo)

SatelliteDescription = _reflection.GeneratedProtocolMessageType('SatelliteDescription', (_message.Message,), {
  'DESCRIPTOR' : _SATELLITEDESCRIPTION,
  '__module__' : 'sat_descrip_pb2'
  # @@protoc_insertion_point(class_scope:LEOHack.SatelliteDescription)
  })
_sym_db.RegisterMessage(SatelliteDescription)

SataliteState = _reflection.GeneratedProtocolMessageType('SataliteState', (_message.Message,), {
  'DESCRIPTOR' : _SATALITESTATE,
  '__module__' : 'sat_descrip_pb2'
  # @@protoc_insertion_point(class_scope:LEOHack.SataliteState)
  })
_sym_db.RegisterMessage(SataliteState)

SystemState = _reflection.GeneratedProtocolMessageType('SystemState', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMSTATE,
  '__module__' : 'sat_descrip_pb2'
  # @@protoc_insertion_point(class_scope:LEOHack.SystemState)
  })
_sym_db.RegisterMessage(SystemState)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'sat_descrip_pb2'
  # @@protoc_insertion_point(class_scope:LEOHack.Command)
  })
_sym_db.RegisterMessage(Command)

ThrustCommand = _reflection.GeneratedProtocolMessageType('ThrustCommand', (_message.Message,), {
  'DESCRIPTOR' : _THRUSTCOMMAND,
  '__module__' : 'sat_descrip_pb2'
  # @@protoc_insertion_point(class_scope:LEOHack.ThrustCommand)
  })
_sym_db.RegisterMessage(ThrustCommand)

CommandReply = _reflection.GeneratedProtocolMessageType('CommandReply', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDREPLY,
  '__module__' : 'sat_descrip_pb2'
  # @@protoc_insertion_point(class_scope:LEOHack.CommandReply)
  })
_sym_db.RegisterMessage(CommandReply)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POSE2D._serialized_start=95
  _POSE2D._serialized_end=140
  _TWIST2D._serialized_start=142
  _TWIST2D._serialized_end=192
  _WRENCH2D._serialized_start=194
  _WRENCH2D._serialized_end=243
  _TEAMINFO._serialized_start=245
  _TEAMINFO._serialized_end=289
  _SATELLITEDESCRIPTION._serialized_start=291
  _SATELLITEDESCRIPTION._serialized_end=400
  _SATALITESTATE._serialized_start=402
  _SATALITESTATE._serialized_end=527
  _SYSTEMSTATE._serialized_start=530
  _SYSTEMSTATE._serialized_end=734
  _SYSTEMSTATE_STATE._serialized_start=686
  _SYSTEMSTATE_STATE._serialized_end=734
  _COMMAND._serialized_start=737
  _COMMAND._serialized_end=870
  _COMMAND_CMDTYPE._serialized_start=795
  _COMMAND_CMDTYPE._serialized_end=870
  _THRUSTCOMMAND._serialized_start=872
  _THRUSTCOMMAND._serialized_end=922
  _COMMANDREPLY._serialized_start=924
  _COMMANDREPLY._serialized_end=955
# @@protoc_insertion_point(module_scope)
