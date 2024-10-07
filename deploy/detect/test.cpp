#include "detect_service.h"

int main()
{
    DetectService detect_service;
    cv::Mat image = cv::imread("E:/DeepLearning/0_DataSets/WorkPiece_Origin/back/0406.jpg");
    std::vector<Object> bboxes;
    auto dst = detect_service.predict(image, bboxes);
    cv::imshow("dst", dst);
    cv::waitKey(0);
}
