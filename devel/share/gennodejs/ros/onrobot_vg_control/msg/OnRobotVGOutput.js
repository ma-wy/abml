// Auto-generated. Do not edit!

// (in-package onrobot_vg_control.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class OnRobotVGOutput {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.rMCA = null;
      this.rVCA = null;
      this.rMCB = null;
      this.rVCB = null;
    }
    else {
      if (initObj.hasOwnProperty('rMCA')) {
        this.rMCA = initObj.rMCA
      }
      else {
        this.rMCA = 0;
      }
      if (initObj.hasOwnProperty('rVCA')) {
        this.rVCA = initObj.rVCA
      }
      else {
        this.rVCA = 0;
      }
      if (initObj.hasOwnProperty('rMCB')) {
        this.rMCB = initObj.rMCB
      }
      else {
        this.rMCB = 0;
      }
      if (initObj.hasOwnProperty('rVCB')) {
        this.rVCB = initObj.rVCB
      }
      else {
        this.rVCB = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OnRobotVGOutput
    // Serialize message field [rMCA]
    bufferOffset = _serializer.uint16(obj.rMCA, buffer, bufferOffset);
    // Serialize message field [rVCA]
    bufferOffset = _serializer.uint16(obj.rVCA, buffer, bufferOffset);
    // Serialize message field [rMCB]
    bufferOffset = _serializer.uint16(obj.rMCB, buffer, bufferOffset);
    // Serialize message field [rVCB]
    bufferOffset = _serializer.uint16(obj.rVCB, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OnRobotVGOutput
    let len;
    let data = new OnRobotVGOutput(null);
    // Deserialize message field [rMCA]
    data.rMCA = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [rVCA]
    data.rVCA = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [rMCB]
    data.rMCB = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [rVCB]
    data.rVCB = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'onrobot_vg_control/OnRobotVGOutput';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4d69df47809c592e1c34e330d53678dd';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # rMCA : The Control mode
    # rVCA : The Target vacuume field
    #
    #        The register allows for control of channel A.
    #        The register is split into two 8-bit fields:
    #        Bits 15-8        Bits 7-0
    #        Control mode     Target vacuum
    #
    #        The Control mode field must contain one of these three values:
    #
    #        Value    Name    Description
    #        0 (0x00) Release Commands the channel to release
    #                         any work item and stop the pump,
    #                         if not required by the other channel.
    #        1 (0x01) Grip    Commands the channel to build up
    #                         and maintain vacuum on this channel.
    #        2 (0x02) Idle    Commands the channel to neither release nor grip.
    #                         Workpieces may "stick" to the channel
    #                         if physically pressed towards its vacuum cups,
    #                         but the VG will use slightly less power.
    #
    #        The Target vacuum field sets the level of vacuum
    #        to be build up and maintained by the chann el.
    #        It is used only when the control mode is 1 (0x01) / Grip.
    #        The target vacuum should be provided in % vacuum.
    #        It should never exceed 80.
    #
    #        Examples:
    #        Setting the register value 0 (0x0000)
    #            will command the VG to release the work item.
    #        Setting the register value 276 (0x0114)
    #            will command the VG to grip at 20 % vacuum.
    #        Setting the register value 296 (0x0128)
    #            will command the VG to grip at 40 % vacuum.
    #        Setting the register value 331 (0x014B)
    #            will command the VG to grip at 75 % vacuum.
    #        Setting the register value 512 (0x0200)
    #            will command the VG to idle the channel.
    
    uint16 rMCA
    uint16 rVCA
    
    # rVCB : Same as the one of channel A.
    
    uint16 rMCB
    uint16 rVCB
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new OnRobotVGOutput(null);
    if (msg.rMCA !== undefined) {
      resolved.rMCA = msg.rMCA;
    }
    else {
      resolved.rMCA = 0
    }

    if (msg.rVCA !== undefined) {
      resolved.rVCA = msg.rVCA;
    }
    else {
      resolved.rVCA = 0
    }

    if (msg.rMCB !== undefined) {
      resolved.rMCB = msg.rMCB;
    }
    else {
      resolved.rMCB = 0
    }

    if (msg.rVCB !== undefined) {
      resolved.rVCB = msg.rVCB;
    }
    else {
      resolved.rVCB = 0
    }

    return resolved;
    }
};

module.exports = OnRobotVGOutput;
