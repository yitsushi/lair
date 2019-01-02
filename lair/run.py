import sys
import argparse
from lair.project_generator import ProjectGenerator


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Service Example')
    parser.add_argument('--project-name', help='Name of the project',
                        type=str, default=None, required=False)
    parser.add_argument('--dependencies',
                        help='Dependencies (comma separated list)',
                        type=str, default="flask,konfig", required=False)
    args = parser.parse_args(args=args)
    args.dependencies = [x for x in args.dependencies.split(',') if x != '']

    app = ProjectGenerator()
    app.set('project-name', args.project_name)
    app.set('dependencies', args.dependencies)

    try:
        app.initialize()
    except Exception as e:
        print("!!!", e)
        return
    app.create()


if __name__ == '__main__':
    main()
