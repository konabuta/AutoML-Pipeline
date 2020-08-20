#  AutoML Pipeline on Azure Machine Learning
Azure Machine Learning が提供する **自動機械学習 (AutoML)** のモデル学習・推論を **再利用可能なパイプライン** として実装します。


- 自動機械学習 (AutoML) とは
    - https://docs.microsoft.com/ja-jp/azure/machine-learning/concept-automated-ml
- Azure Machine Learning Pipeline とは
    - https://docs.microsoft.com/ja-jp/azure/machine-learning/concept-ml-pipelines


---


# Sample Code & Notebook


### データの準備
データは Livedoor ニュースのコーパスを利用します。
*  Notebook : [data-prep.ipynb](notebooks/data-prep.ipynb)


### AutoML (Python SDK) による日本語分類モデルの構築
Azure ML Python SDK を利用して、AutoML による BERT を特徴量抽出に活用した日本語分類モデルを構築します。
* Notebook : [automl-classification-Force-text-dnn.ipynb](notebooks/automl-classification-Force-text-dnn.ipynb)


### Machine Learning Pipeline による AutoML モデルの推論パイプライン作成
Azure Machine Learning の Pipeline 機能を利用して、AutoML で構築したモデルの*推論*を行う再利用可能なパイプラインを作成します。
* Notebook : [automl-inference-pipeline.ipynb](notebooks/automl-inference-pipeline.ipynb)


### Machine Learning Pipeline による AutoML モデルの学習パイプライン作成
Azure Machine Learning の Pipeline 機能を利用して、AutoML によるモデルの*学習*を行う再利用可能なパイプラインを作成します。
* Notebook : [automl-train-pipeline.ipynb](notebooks/automl-train-pipeline.ipynb)


## その他
####  Machine Learning Pipeline を **トリガー** する方法
- [ロジック アプリから Machine Learning パイプラインの実行をトリガーする](https://docs.microsoft.com/ja-JP/azure/machine-learning/how-to-trigger-published-pipeline)
- [Azure Machine Learning パイプラインを Azure Data Factory で実行する
](https://docs.microsoft.com/ja-jp/azure/data-factory/transform-data-machine-learning-service)

```python

```
