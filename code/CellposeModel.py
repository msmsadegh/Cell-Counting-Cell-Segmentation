from cellpose import models

def train_cellpose(train_folder, test_folder):
    # Set your desired parameters
    use_gpu = True
    fast_mode = True
    chan = 2
    n_epochs = 50
    learning_rate = 0.0002
    batch_size = 8
    img_filter = 'img'
    mask_filter = 'masks'
    verbose = True

    # Create a model
    model = models.CellposeModel(gpu=use_gpu, model_type='cyto')

    # Load your training data and labels (replace this with your actual loading logic)
    train_data = ...
    train_labels = ...

    # Train the model using models.train method
    model.train(train_data, train_labels,
                # train_files=None,  # replace with your actual train_files
                # test_data=None,  # replace with your actual test_data
                # test_labels=None,  # replace with your actual test_labels
                # test_files=None,  # replace with your actual test_files
                channels=[chan, 0],
                normalize=True,
                save_path='.',  # replace with your desired save path
                save_every=100,
                save_each=False,
                learning_rate=learning_rate,
                n_epochs=n_epochs,
                momentum=0.9,
                SGD=True,
                weight_decay=0.00001,
                batch_size=batch_size,
                nimg_per_epoch=None,
                rescale=True,
                min_train_masks=5,
                model_name=None)

if __name__ == "__main__":
    train_folder = "/Users/mohammadsadegh/PycharmProjects/cellpose/dataset/pv_ab/train_folder"
    test_folder = "/Users/mohammadsadegh/PycharmProjects/cellpose/dataset/pv_ab/test_folder"
    train_cellpose(train_folder, test_folder)
