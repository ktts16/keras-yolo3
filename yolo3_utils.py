import numpy as np

# Source: https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
def IOU(boxA, boxB):
	# determine the (x, y)-coordinates of the intersection rectangle
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])

	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

	# compute the area of both the prediction and ground-truth
	# rectangles
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(boxAArea + boxBArea - interArea)

	# return the intersection over union value
	return iou


def classification_accuracy_one_image(actual_boxes, predicted_boxes, actual_classes, predicted_classes, print_log=False, iou_threshold=0.5):
    correct = 0
    if len(predicted_boxes) == 0:
        return 0
    for ba, ca in zip(actual_boxes, actual_classes):
        iou_vals = np.asarray([IOU(tbp[:4], ba[:4]) for tbp in predicted_boxes])
        max_indices = np.argwhere(iou_vals == np.amax(iou_vals))
#         if print_log:    print(max_indices)
#         if print_log:    print(iou_vals[max_indices[0]], ba, predicted_boxes[max_indices[0]])
        if len(max_indices) == 1 and iou_vals[max_indices[0]] >= iou_threshold \
        and predicted_classes[max_indices[0]] == ca: #predicted class == actual class
            correct = correct + 1
            if print_log:    print(iou_vals[max_indices[0]], ba, predicted_boxes[max_indices[0]])
    return correct / len(actual_boxes) # classification rate


def all_equals(l, n = 0):
    return all(v == n for v in l)
#-- test
# print(all_equals([0, 0, 0, 0, 0]))
# print(all_equals([1.0, 2.0, 3.0, 4.0, 0]))


def copy_and_swap_columns(array_2d, from_col_indices):
    new_array_2d = np.zeros(array_2d.shape)
    for i, o in enumerate(from_col_indices):
        new_array_2d[:,i] = array_2d[:,o]
    return new_array_2d
