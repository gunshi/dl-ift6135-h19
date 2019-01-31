import argparse
import datetime
import os


def get_params():

    # ARGS
    parser = argparse.ArgumentParser(description='PyTorch Cats & Dogs')

    # Paths
    parser.add_argument('--data_path', type=str,
                        help='Path to data : Images Folder')
    parser.add_argument('--out_path', type=str,
                        help='Path to data : Directory out: a/b/exp1 (-> a/b/<TIME>_exp1)')

    # Training params
    parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                        help='input batch size for training (default: 64)')
    parser.add_argument('--valid-split', type=float, default=0.1, help='Ratio of train-val split (e.g. 0.2)')
    parser.add_argument('--epochs', type=int, default=10, metavar='N',
                        help='number of epochs to train (default: 10)')
    parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                        help='learning rate (default: 0.01)')
    parser.add_argument('--momentum', type=float, default=0.5, metavar='M',
                        help='SGD momentum (default: 0.5)')

    # CUDA
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')

    parser.add_argument('--seed', type=int, default=29, metavar='S',
                        help='random seed (default: 1)')

    # Intervals
    parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                        help='how many batches to wait before logging training status')
    parser.add_argument('--model-save-interval', type=int, default=100, metavar='N',
                        help='how many batches to wait before saving model')

    # Image transforms
    parser.add_argument('--dont_shuffle', action='store_true')
    parser.add_argument('--dont_drop_last', action='store_true', help="Whether not to drop the last batch in dataset if its size < batch_size")
    parser.add_argument('--dont_resize', action='store_true', help="Whether not to resize images")
    parser.add_argument('--imsize', type=int, default=64)
    parser.add_argument('--centercrop', action='store_true', help="Whether to center crop images")
    parser.add_argument('--centercrop_size', type=int, default=128)
    parser.add_argument('--dont_tanh_scale', action='store_true', help="Whether to scale image values to -1->1")
    parser.add_argument('--normalize', action='store_true', help="Whether to normalize image values")

    args = parser.parse_args()

    args.shuffle = not args.dont_shuffle
    args.drop_last = not args.dont_drop_last
    args.resize = not args.dont_resize
    args.tanh_scale = not args.dont_tanh_scale

    args.out_path = os.path.join(os.path.dirname(args.out_path),
                                 '{0:%Y%m%d_%H%M%S}_{1}'.format(datetime.datetime.now(), os.path.basename(args.out_path)))

    return args
