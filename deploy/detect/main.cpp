#include "opencv2/opencv.hpp"
#include "yolov8.h"
#include <chrono>

const std::vector<std::string> CLASS_NAMES = {
    "work_piece",
};

const std::vector<std::vector<unsigned int>> COLORS = {
    {0, 114, 189},
};

int main(int argc, char **argv)
{
    const std::string engine_file_path = "E:/DeepLearning/yolo-utils/yolov8n.engine";
    const std::string path = "E:/DeepLearning/0_DataSets/WorkPiece_Origin/back/"; // 图片所在的文件夹
    std::vector<std::string> imagePathList;
    cv::glob(path + "/*.jpg", imagePathList);

    cudaSetDevice(0);
    auto yolov8 = new YOLOv8(engine_file_path);
    yolov8->make_pipe(true);

    cv::Mat res, image;
    cv::Size size = cv::Size{800, 800};
    int num_labels = 1;
    int topk = 100;
    float score_thres = 0.25f;
    float iou_thres = 0.65f;

    std::vector<Object> objs;

    cv::namedWindow("result", cv::WINDOW_AUTOSIZE);

    for (auto &p : imagePathList)
    {
        objs.clear();
        image = cv::imread(p);
        yolov8->copy_from_Mat(image, size);
        auto start = std::chrono::system_clock::now();
        yolov8->infer();
        auto end = std::chrono::system_clock::now();
        yolov8->postprocess(objs, score_thres, iou_thres, topk, num_labels);
        yolov8->draw_objects(image, res, objs, CLASS_NAMES, COLORS);
        auto tc = (double)std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() / 1000.;
        printf("cost %2.4lf ms\n", tc);
        cv::imshow("result", res);
        cv::waitKey(0);
    }

    cv::destroyAllWindows();
    delete yolov8;
    return 0;
}
