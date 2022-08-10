import argparse
from bagels.bagels import bagels


def bagels_cmd():
    parser = argparse.ArgumentParser(
        description="세 자리 수 맞추기 게임"
    )

    parser.add_argument("--limit", action="store", type=int, required=False,
                        help="추측 횟수 제한 하기")
    args = parser.parse_args()
    bagels(_limit=args.limit)
