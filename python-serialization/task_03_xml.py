#!/usr/bin/python3
"""Serializing and Desarializing XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serializing Python dictionary into XML"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key).text = value

    ET.ElementTree(root).write(filename)


def deserialize_from_xml(filename):
    """deserializing XML to Python dictionary"""
    tree = ET.parse(filename)       # Loading the XML
    root = tree.getroot()           # Retrieving <data> root
    result = {}                     # Initializing an empty dict

    for child in root:              # Read through each child tag
        result[child.tag] = child.text  # Adding in the dict

    return result
