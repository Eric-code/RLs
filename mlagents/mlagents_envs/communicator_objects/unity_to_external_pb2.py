# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlagents_envs/communicator_objects/unity_to_external.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mlagents_envs.communicator_objects import unity_message_pb2 as mlagents__envs_dot_communicator__objects_dot_unity__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mlagents_envs/communicator_objects/unity_to_external.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_pb=_b('\n:mlagents_envs/communicator_objects/unity_to_external.proto\x12\x14\x63ommunicator_objects\x1a\x36mlagents_envs/communicator_objects/unity_message.proto2v\n\x14UnityToExternalProto\x12^\n\x08\x45xchange\x12\'.communicator_objects.UnityMessageProto\x1a\'.communicator_objects.UnityMessageProto\"\x00\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
  ,
  dependencies=[mlagents__envs_dot_communicator__objects_dot_unity__message__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\034MLAgents.CommunicatorObjects'))

_UNITYTOEXTERNALPROTO = _descriptor.ServiceDescriptor(
  name='UnityToExternalProto',
  full_name='communicator_objects.UnityToExternalProto',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=140,
  serialized_end=258,
  methods=[
  _descriptor.MethodDescriptor(
    name='Exchange',
    full_name='communicator_objects.UnityToExternalProto.Exchange',
    index=0,
    containing_service=None,
    input_type=mlagents__envs_dot_communicator__objects_dot_unity__message__pb2._UNITYMESSAGEPROTO,
    output_type=mlagents__envs_dot_communicator__objects_dot_unity__message__pb2._UNITYMESSAGEPROTO,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_UNITYTOEXTERNALPROTO)

DESCRIPTOR.services_by_name['UnityToExternalProto'] = _UNITYTOEXTERNALPROTO

# @@protoc_insertion_point(module_scope)