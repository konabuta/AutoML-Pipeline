#  AutoML Pipeline on Azure Machine Learning


## データの準備
データは Livedoor ニュースのコーパスを利用します。
*  Notebook : [data-prep.ipynb](notebooks/data-prep.ipynb)


## AutoML (Python SDK) による日本語分類モデルの構築
Azure ML Python SDK を利用して、AutoML による BERT を特徴量抽出に活用した日本語分類モデルを構築します。
* Notebook : [automl-classification-Force-text-dnn.ipynb](notebooks/automl-classification-Force-text-dnn.ipynb)

## Machine Learning Pipeline による AutoML モデルの推論パイプライン作成
Azure Machine Learning の Pipeline 機能を利用して、AutoML で構築したモデルの*推論*を行う再利用可能なパイプラインを作成します。
* Notebook : [automl-inference-pipeline.ipynb](notebooks/automl-inference-pipeline.ipynb)

## Machine Learning Pipeline による AutoML モデルの学習パイプライン作成
Azure Machine Learning の Pipeline 機能を利用して、AutoML によるモデルの*学習*を行う再利用可能なパイプラインを作成します。
* Notebook : [automl-train-pipeline.ipynb](notebooks/automl-train-pipeline.ipynb)

