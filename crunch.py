#!/usr/bin/env python3

import io


class DataInfo:
    def __init__(self, histogram, num_lines):
        self.histogram = histogram
        self.num_lines = num_lines


def _num_lines(stream):
    num = 0
    stream.seek(0)
    for _ in stream.readlines():
        num += 1

    return num


def _histogram(stream):
    hist = [0] * 16

    stream.seek(0)
    while len(buf := stream.read(16)) > 0:
        for b in buf:
            hist[b // 16] += 1

    return hist


def crunch(stream):
    return DataInfo(_histogram(stream), _num_lines(stream))


def dump_data_info(di):
    print(f"histogram {di.histogram}\nlines: {di.num_lines}")


dump_data_info(crunch(open("environment.yml", "rb")))
print("---")
dump_data_info(crunch(io.BytesIO(b"\x00\x01\x10\x22")))
