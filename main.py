import sys

import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon, QPixmap

from task5 import ClassedAnnotationIterator, ClassedDatasetIterator
from task1 import save_as_csv, scan_dataset
from task2 import copy_dataset, scan_annotation
from task3 import randomized_dataset_copy


class MainWindow():
    def __init__(self)-> None:
        super().__init__()


def main() -> None:

    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()