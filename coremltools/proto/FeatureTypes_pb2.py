# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FeatureTypes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x46\x65\x61tureTypes.proto\x12\x14\x43oreML.Specification\"\x12\n\x10Int64FeatureType\"\x13\n\x11\x44oubleFeatureType\"\x13\n\x11StringFeatureType\"3\n\tSizeRange\x12\x12\n\nlowerBound\x18\x01 \x01(\x04\x12\x12\n\nupperBound\x18\x02 \x01(\x03\"\x95\x05\n\x10ImageFeatureType\x12\r\n\x05width\x18\x01 \x01(\x03\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12V\n\x0f\x65numeratedSizes\x18\x15 \x01(\x0b\x32;.CoreML.Specification.ImageFeatureType.EnumeratedImageSizesH\x00\x12O\n\x0eimageSizeRange\x18\x1f \x01(\x0b\x32\x35.CoreML.Specification.ImageFeatureType.ImageSizeRangeH\x00\x12\x45\n\ncolorSpace\x18\x03 \x01(\x0e\x32\x31.CoreML.Specification.ImageFeatureType.ColorSpace\x1a*\n\tImageSize\x12\r\n\x05width\x18\x01 \x01(\x04\x12\x0e\n\x06height\x18\x02 \x01(\x04\x1aW\n\x14\x45numeratedImageSizes\x12?\n\x05sizes\x18\x01 \x03(\x0b\x32\x30.CoreML.Specification.ImageFeatureType.ImageSize\x1a{\n\x0eImageSizeRange\x12\x33\n\nwidthRange\x18\x01 \x01(\x0b\x32\x1f.CoreML.Specification.SizeRange\x12\x34\n\x0bheightRange\x18\x02 \x01(\x0b\x32\x1f.CoreML.Specification.SizeRange\"]\n\nColorSpace\x12\x17\n\x13INVALID_COLOR_SPACE\x10\x00\x12\r\n\tGRAYSCALE\x10\n\x12\x07\n\x03RGB\x10\x14\x12\x07\n\x03\x42GR\x10\x1e\x12\x15\n\x11GRAYSCALE_FLOAT16\x10(B\x11\n\x0fSizeFlexibility\"\x9d\x05\n\x10\x41rrayFeatureType\x12\r\n\x05shape\x18\x01 \x03(\x03\x12\x46\n\x08\x64\x61taType\x18\x02 \x01(\x0e\x32\x34.CoreML.Specification.ArrayFeatureType.ArrayDataType\x12S\n\x10\x65numeratedShapes\x18\x15 \x01(\x0b\x32\x37.CoreML.Specification.ArrayFeatureType.EnumeratedShapesH\x00\x12G\n\nshapeRange\x18\x1f \x01(\x0b\x32\x31.CoreML.Specification.ArrayFeatureType.ShapeRangeH\x00\x12\x19\n\x0fintDefaultValue\x18) \x01(\x05H\x01\x12\x1b\n\x11\x66loatDefaultValue\x18\x33 \x01(\x02H\x01\x12\x1c\n\x12\x64oubleDefaultValue\x18= \x01(\x01H\x01\x1a\x16\n\x05Shape\x12\r\n\x05shape\x18\x01 \x03(\x03\x1aP\n\x10\x45numeratedShapes\x12<\n\x06shapes\x18\x01 \x03(\x0b\x32,.CoreML.Specification.ArrayFeatureType.Shape\x1a\x41\n\nShapeRange\x12\x33\n\nsizeRanges\x18\x01 \x03(\x0b\x32\x1f.CoreML.Specification.SizeRange\"e\n\rArrayDataType\x12\x1b\n\x17INVALID_ARRAY_DATA_TYPE\x10\x00\x12\r\n\x07\x46LOAT32\x10\xa0\x80\x04\x12\x0c\n\x06\x44OUBLE\x10\xc0\x80\x04\x12\x0b\n\x05INT32\x10\xa0\x80\x08\x12\r\n\x07\x46LOAT16\x10\x90\x80\x04\x42\x12\n\x10ShapeFlexibilityB\x16\n\x14\x64\x65\x66\x61ultOptionalValue\"\xa4\x01\n\x15\x44ictionaryFeatureType\x12>\n\x0cint64KeyType\x18\x01 \x01(\x0b\x32&.CoreML.Specification.Int64FeatureTypeH\x00\x12@\n\rstringKeyType\x18\x02 \x01(\x0b\x32\'.CoreML.Specification.StringFeatureTypeH\x00\x42\t\n\x07KeyType\"\xcd\x01\n\x13SequenceFeatureType\x12;\n\tint64Type\x18\x01 \x01(\x0b\x32&.CoreML.Specification.Int64FeatureTypeH\x00\x12=\n\nstringType\x18\x03 \x01(\x0b\x32\'.CoreML.Specification.StringFeatureTypeH\x00\x12\x32\n\tsizeRange\x18\x65 \x01(\x0b\x32\x1f.CoreML.Specification.SizeRangeB\x06\n\x04Type\"W\n\x10StateFeatureType\x12;\n\tarrayType\x18\x01 \x01(\x0b\x32&.CoreML.Specification.ArrayFeatureTypeH\x00\x42\x06\n\x04Type\"\xab\x04\n\x0b\x46\x65\x61tureType\x12;\n\tint64Type\x18\x01 \x01(\x0b\x32&.CoreML.Specification.Int64FeatureTypeH\x00\x12=\n\ndoubleType\x18\x02 \x01(\x0b\x32\'.CoreML.Specification.DoubleFeatureTypeH\x00\x12=\n\nstringType\x18\x03 \x01(\x0b\x32\'.CoreML.Specification.StringFeatureTypeH\x00\x12;\n\timageType\x18\x04 \x01(\x0b\x32&.CoreML.Specification.ImageFeatureTypeH\x00\x12@\n\x0emultiArrayType\x18\x05 \x01(\x0b\x32&.CoreML.Specification.ArrayFeatureTypeH\x00\x12\x45\n\x0e\x64ictionaryType\x18\x06 \x01(\x0b\x32+.CoreML.Specification.DictionaryFeatureTypeH\x00\x12\x41\n\x0csequenceType\x18\x07 \x01(\x0b\x32).CoreML.Specification.SequenceFeatureTypeH\x00\x12;\n\tstateType\x18\x08 \x01(\x0b\x32&.CoreML.Specification.StateFeatureTypeH\x00\x12\x13\n\nisOptional\x18\xe8\x07 \x01(\x08\x42\x06\n\x04TypeB\x02H\x03\x62\x06proto3')



_INT64FEATURETYPE = DESCRIPTOR.message_types_by_name['Int64FeatureType']
_DOUBLEFEATURETYPE = DESCRIPTOR.message_types_by_name['DoubleFeatureType']
_STRINGFEATURETYPE = DESCRIPTOR.message_types_by_name['StringFeatureType']
_SIZERANGE = DESCRIPTOR.message_types_by_name['SizeRange']
_IMAGEFEATURETYPE = DESCRIPTOR.message_types_by_name['ImageFeatureType']
_IMAGEFEATURETYPE_IMAGESIZE = _IMAGEFEATURETYPE.nested_types_by_name['ImageSize']
_IMAGEFEATURETYPE_ENUMERATEDIMAGESIZES = _IMAGEFEATURETYPE.nested_types_by_name['EnumeratedImageSizes']
_IMAGEFEATURETYPE_IMAGESIZERANGE = _IMAGEFEATURETYPE.nested_types_by_name['ImageSizeRange']
_ARRAYFEATURETYPE = DESCRIPTOR.message_types_by_name['ArrayFeatureType']
_ARRAYFEATURETYPE_SHAPE = _ARRAYFEATURETYPE.nested_types_by_name['Shape']
_ARRAYFEATURETYPE_ENUMERATEDSHAPES = _ARRAYFEATURETYPE.nested_types_by_name['EnumeratedShapes']
_ARRAYFEATURETYPE_SHAPERANGE = _ARRAYFEATURETYPE.nested_types_by_name['ShapeRange']
_DICTIONARYFEATURETYPE = DESCRIPTOR.message_types_by_name['DictionaryFeatureType']
_SEQUENCEFEATURETYPE = DESCRIPTOR.message_types_by_name['SequenceFeatureType']
_STATEFEATURETYPE = DESCRIPTOR.message_types_by_name['StateFeatureType']
_FEATURETYPE = DESCRIPTOR.message_types_by_name['FeatureType']
_IMAGEFEATURETYPE_COLORSPACE = _IMAGEFEATURETYPE.enum_types_by_name['ColorSpace']
_ARRAYFEATURETYPE_ARRAYDATATYPE = _ARRAYFEATURETYPE.enum_types_by_name['ArrayDataType']
Int64FeatureType = _reflection.GeneratedProtocolMessageType('Int64FeatureType', (_message.Message,), {
  'DESCRIPTOR' : _INT64FEATURETYPE,
  '__module__' : 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.Int64FeatureType)
  })
_sym_db.RegisterMessage(Int64FeatureType)

DoubleFeatureType = _reflection.GeneratedProtocolMessageType('DoubleFeatureType', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLEFEATURETYPE,
  '__module__' : 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.DoubleFeatureType)
  })
_sym_db.RegisterMessage(DoubleFeatureType)

StringFeatureType = _reflection.GeneratedProtocolMessageType('StringFeatureType', (_message.Message,), {
  'DESCRIPTOR' : _STRINGFEATURETYPE,
  '__module__' : 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.StringFeatureType)
  })
_sym_db.RegisterMessage(StringFeatureType)

SizeRange = _reflection.GeneratedProtocolMessageType('SizeRange', (_message.Message,), {
  'DESCRIPTOR' : _SIZERANGE,
  '__module__' : 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.SizeRange)
  })
_sym_db.RegisterMessage(SizeRange)

ImageFeatureType = _reflection.GeneratedProtocolMessageType('ImageFeatureType', (_message.Message,), {

  'ImageSize' : _reflection.GeneratedProtocolMessageType('ImageSize', (_message.Message,), {
    'DESCRIPTOR' : _IMAGEFEATURETYPE_IMAGESIZE,
    '__module__' : 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ImageFeatureType.ImageSize)
    })
  ,

  'EnumeratedImageSizes' : _reflection.GeneratedProtocolMessageType('EnumeratedImageSizes', (_message.Message,), {
    'DESCRIPTOR' : _IMAGEFEATURETYPE_ENUMERATEDIMAGESIZES,
    '__module__' : 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ImageFeatureType.EnumeratedImageSizes)
    })
  ,

  'ImageSizeRange' : _reflection.GeneratedProtocolMessageType('ImageSizeRange', (_message.Message,), {
    'DESCRIPTOR' : _IMAGEFEATURETYPE_IMAGESIZERANGE,
    '__module__' : 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ImageFeatureType.ImageSizeRange)
    })
  ,
  'DESCRIPTOR' : _IMAGEFEATURETYPE,
  '__module__' : 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.ImageFeatureType)
  })
_sym_db.RegisterMessage(ImageFeatureType)
_sym_db.RegisterMessage(ImageFeatureType.ImageSize)
_sym_db.RegisterMessage(ImageFeatureType.EnumeratedImageSizes)
_sym_db.RegisterMessage(ImageFeatureType.ImageSizeRange)

ArrayFeatureType = _reflection.GeneratedProtocolMessageType('ArrayFeatureType', (_message.Message,), {

  'Shape' : _reflection.GeneratedProtocolMessageType('Shape', (_message.Message,), {
    'DESCRIPTOR' : _ARRAYFEATURETYPE_SHAPE,
    '__module__' : 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ArrayFeatureType.Shape)
    })
  ,

  'EnumeratedShapes' : _reflection.GeneratedProtocolMessageType('EnumeratedShapes', (_message.Message,), {
    'DESCRIPTOR' : _ARRAYFEATURETYPE_ENUMERATEDSHAPES,
    '__module__' : 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ArrayFeatureType.EnumeratedShapes)
    })
  ,

  'ShapeRange' : _reflection.GeneratedProtocolMessageType('ShapeRange', (_message.Message,), {
    'DESCRIPTOR' : _ARRAYFEATURETYPE_SHAPERANGE,
    '__module__' : 'FeatureTypes_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.ArrayFeatureType.ShapeRange)
    })
  ,
  'DESCRIPTOR' : _ARRAYFEATURETYPE,
  '__module__' : 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.ArrayFeatureType)
  })
_sym_db.RegisterMessage(ArrayFeatureType)
_sym_db.RegisterMessage(ArrayFeatureType.Shape)
_sym_db.RegisterMessage(ArrayFeatureType.EnumeratedShapes)
_sym_db.RegisterMessage(ArrayFeatureType.ShapeRange)

DictionaryFeatureType = _reflection.GeneratedProtocolMessageType('DictionaryFeatureType', (_message.Message,), {
  'DESCRIPTOR' : _DICTIONARYFEATURETYPE,
  '__module__' : 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.DictionaryFeatureType)
  })
_sym_db.RegisterMessage(DictionaryFeatureType)

SequenceFeatureType = _reflection.GeneratedProtocolMessageType('SequenceFeatureType', (_message.Message,), {
  'DESCRIPTOR' : _SEQUENCEFEATURETYPE,
  '__module__' : 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.SequenceFeatureType)
  })
_sym_db.RegisterMessage(SequenceFeatureType)

StateFeatureType = _reflection.GeneratedProtocolMessageType('StateFeatureType', (_message.Message,), {
  'DESCRIPTOR' : _STATEFEATURETYPE,
  '__module__' : 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.StateFeatureType)
  })
_sym_db.RegisterMessage(StateFeatureType)

FeatureType = _reflection.GeneratedProtocolMessageType('FeatureType', (_message.Message,), {
  'DESCRIPTOR' : _FEATURETYPE,
  '__module__' : 'FeatureTypes_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.FeatureType)
  })
_sym_db.RegisterMessage(FeatureType)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003'
  _INT64FEATURETYPE._serialized_start=44
  _INT64FEATURETYPE._serialized_end=62
  _DOUBLEFEATURETYPE._serialized_start=64
  _DOUBLEFEATURETYPE._serialized_end=83
  _STRINGFEATURETYPE._serialized_start=85
  _STRINGFEATURETYPE._serialized_end=104
  _SIZERANGE._serialized_start=106
  _SIZERANGE._serialized_end=157
  _IMAGEFEATURETYPE._serialized_start=160
  _IMAGEFEATURETYPE._serialized_end=821
  _IMAGEFEATURETYPE_IMAGESIZE._serialized_start=451
  _IMAGEFEATURETYPE_IMAGESIZE._serialized_end=493
  _IMAGEFEATURETYPE_ENUMERATEDIMAGESIZES._serialized_start=495
  _IMAGEFEATURETYPE_ENUMERATEDIMAGESIZES._serialized_end=582
  _IMAGEFEATURETYPE_IMAGESIZERANGE._serialized_start=584
  _IMAGEFEATURETYPE_IMAGESIZERANGE._serialized_end=707
  _IMAGEFEATURETYPE_COLORSPACE._serialized_start=709
  _IMAGEFEATURETYPE_COLORSPACE._serialized_end=802
  _ARRAYFEATURETYPE._serialized_start=824
  _ARRAYFEATURETYPE._serialized_end=1493
  _ARRAYFEATURETYPE_SHAPE._serialized_start=1175
  _ARRAYFEATURETYPE_SHAPE._serialized_end=1197
  _ARRAYFEATURETYPE_ENUMERATEDSHAPES._serialized_start=1199
  _ARRAYFEATURETYPE_ENUMERATEDSHAPES._serialized_end=1279
  _ARRAYFEATURETYPE_SHAPERANGE._serialized_start=1281
  _ARRAYFEATURETYPE_SHAPERANGE._serialized_end=1346
  _ARRAYFEATURETYPE_ARRAYDATATYPE._serialized_start=1348
  _ARRAYFEATURETYPE_ARRAYDATATYPE._serialized_end=1449
  _DICTIONARYFEATURETYPE._serialized_start=1496
  _DICTIONARYFEATURETYPE._serialized_end=1660
  _SEQUENCEFEATURETYPE._serialized_start=1663
  _SEQUENCEFEATURETYPE._serialized_end=1868
  _STATEFEATURETYPE._serialized_start=1870
  _STATEFEATURETYPE._serialized_end=1957
  _FEATURETYPE._serialized_start=1960
  _FEATURETYPE._serialized_end=2515
# @@protoc_insertion_point(module_scope)
