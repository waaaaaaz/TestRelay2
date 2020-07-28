# coding: utf-8
import os
import sys
import log
import argparse

""" global project path settings """
project_path = os.path.abspath(
    os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)), os.pardir))
sys.path.insert(0, project_path)

from test_relay.execute import Execute
from test_relay.model.suite import Suite

script_path = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
case_path = os.path.abspath(os.path.join(script_path, "test_suite"))


def parse_options():
    parser = argparse.ArgumentParser(usage="省钱快报接口自动化测试执行入口")

    parser.add_argument(
        '-S',
        '--sys',
        default="SQKB",
        help="指定被测系统, MOSES或者NUANNUAN, 默认值是MOSES"

    )

    parser.add_argument(
        '-E',
        '--env',
        default="DEV",
        help="指定执行环境, DEV环境还是BETA环境或者PROD环境, 默认值是TEST"
    )

    parser.add_argument(
        '-T',
        '--tags',
        nargs='+',
        default=None,
        help="指定用例标签, 多标签取并集; 默认值为None, 对所有标签的用例生效"
    )

    parser.add_argument(
        '-P',
        '--path',
        nargs='+',
        default="test_suite",
        help="指定用例路径, 用例在工程中的相对路径; 必须要'test_suite'路径下; 可以是个文件夹也可以是个文件; 文件夹下所有用例递归执行; 多个路径取并集; 默认值是所有用例的父路径"
    )

    parser.add_argument(
        '-L',
        '--loglevel',
        default="INFO",
        help="指定执行时的日志级别; 选项为DEBUG/INFO/WARNING/ERROR/CRITICAL; 默认为INFO "
    )

    parser.add_argument(
        '--logfile',
        default="logs",
        help="指定执行时的日志路径; 默认为工程路径 "
    )

    args = parser.parse_args()

    return parser, args


def __get_abspath(file_path):
    return os.path.abspath(file_path)


def __is_sub_path(file_path):
    return __get_abspath(file_path).startswith(case_path)


def __is_test_file(file_path):
    return os.path.isfile(file_path) and __get_abspath(file_path).endswith(".json")


def __is_file(file):
    return os.path.isfile(file)


def __find__test_files(file_list):
    all_case_file = []
    for file_path in file_list:
        if __is_file(file_path):
            all_case_file.append(__get_abspath(file_path))
        else:
            for dir_path, dir_names, file_names in os.walk(__get_abspath(file_path)):
                for f in file_names:
                    file_abs_name = os.path.join(dir_path, f)
                    if __is_test_file(file_abs_name):
                        all_case_file.append(file_abs_name)
    return list(set(all_case_file))


def main():
    parser, args = parse_options()

    if args.sys.lower() not in ["sqkb", "nuannuan"]:
        print("被测系统参数指定错误; 使用 --help 命令查看详情")
        sys.exit(1)
    else:
        print("当前被测系统是: {0}".format(args.sys.upper()))

    if args.env.lower() not in ["dev", "beta", "prod"]:
        print("被测环境参数指定错误; 使用 --help 命令查看详情")
        sys.exit(1)
    else:
        print("当前执行环境是: {0}".format(args.env.upper()))

    if args.tags is None:
        print("当前执行没有指定用例标签")
    else:
        print("当前执行指定的用例标签是: ")
        for t in args.tags:
            print("{0}".format(t))

    available_paths = []
    for p in args.path:
        if not __is_sub_path(p):
            print("{0} 不是有效的用例路径; 使用 --help 命令查看详情".format(p))
            sys.exit(1)
        else:
            available_paths.append(p)
            print("当前执行的用例路径是: ")
            for ap in available_paths:
                print("{0}".format(ap))

    available_case_files = __find__test_files(available_paths)

    if len(available_case_files) == 0:
        print("没有找到可用的用例文件")
        sys.exit(1)
    else:
        print("当前执行的用例文件是: ")
        for cf in available_case_files:
            print("{0}".format(cf))

    case_execution = Execute(args.sys, args.env, args.tags, available_case_files)
    case_execution.test()


if __name__ == "__main__":
    main()
