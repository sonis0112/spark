#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import overload
from typing import Any, List, Optional, Tuple, Type
from pyspark.ml._typing import ParamMap

from pyspark.ml import Estimator, Model
from pyspark.ml.evaluation import Evaluator
from pyspark.ml.param import Param
from pyspark.ml.param.shared import HasCollectSubModels, HasParallelism, HasSeed
from pyspark.ml.util import MLReader, MLReadable, MLWriter, MLWritable

class ParamGridBuilder:
    def __init__(self) -> None: ...
    def addGrid(self, param: Param, values: List[Any]) -> ParamGridBuilder: ...
    @overload
    def baseOn(self, __args: ParamMap) -> ParamGridBuilder: ...
    @overload
    def baseOn(self, *args: Tuple[Param, Any]) -> ParamGridBuilder: ...
    def build(self) -> List[ParamMap]: ...

class _ValidatorParams(HasSeed):
    estimator: Param[Estimator]
    estimatorParamMaps: Param[List[ParamMap]]
    evaluator: Param[Evaluator]
    def getEstimator(self) -> Estimator: ...
    def getEstimatorParamMaps(self) -> List[ParamMap]: ...
    def getEvaluator(self) -> Evaluator: ...

class _CrossValidatorParams(_ValidatorParams):
    numFolds: Param[int]
    foldCol: Param[str]
    def __init__(self, *args: Any): ...
    def getNumFolds(self) -> int: ...
    def getFoldCol(self) -> str: ...

class CrossValidator(
    Estimator[CrossValidatorModel],
    _CrossValidatorParams,
    HasParallelism,
    HasCollectSubModels,
    MLReadable[CrossValidator],
    MLWritable,
):
    def __init__(
        self,
        *,
        estimator: Optional[Estimator] = ...,
        estimatorParamMaps: Optional[List[ParamMap]] = ...,
        evaluator: Optional[Evaluator] = ...,
        numFolds: int = ...,
        seed: Optional[int] = ...,
        parallelism: int = ...,
        collectSubModels: bool = ...,
        foldCol: str = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        estimator: Optional[Estimator] = ...,
        estimatorParamMaps: Optional[List[ParamMap]] = ...,
        evaluator: Optional[Evaluator] = ...,
        numFolds: int = ...,
        seed: Optional[int] = ...,
        parallelism: int = ...,
        collectSubModels: bool = ...,
        foldCol: str = ...
    ) -> CrossValidator: ...
    def setEstimator(self, value: Estimator) -> CrossValidator: ...
    def setEstimatorParamMaps(self, value: List[ParamMap]) -> CrossValidator: ...
    def setEvaluator(self, value: Evaluator) -> CrossValidator: ...
    def setNumFolds(self, value: int) -> CrossValidator: ...
    def setFoldCol(self, value: str) -> CrossValidator: ...
    def setSeed(self, value: int) -> CrossValidator: ...
    def setParallelism(self, value: int) -> CrossValidator: ...
    def setCollectSubModels(self, value: bool) -> CrossValidator: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> CrossValidator: ...
    def write(self) -> MLWriter: ...
    @classmethod
    def read(cls: Type[CrossValidator]) -> MLReader: ...

class CrossValidatorModel(
    Model, _CrossValidatorParams, MLReadable[CrossValidatorModel], MLWritable
):
    bestModel: Model
    avgMetrics: List[float]
    subModels: List[List[Model]]
    def __init__(
        self,
        bestModel: Model,
        avgMetrics: List[float] = ...,
        subModels: Optional[List[List[Model]]] = ...,
    ) -> None: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> CrossValidatorModel: ...
    def write(self) -> MLWriter: ...
    @classmethod
    def read(cls: Type[CrossValidatorModel]) -> MLReader: ...

class _TrainValidationSplitParams(_ValidatorParams):
    trainRatio: Param[float]
    def __init__(self, *args: Any): ...
    def getTrainRatio(self) -> float: ...

class TrainValidationSplit(
    Estimator[TrainValidationSplitModel],
    _TrainValidationSplitParams,
    HasParallelism,
    HasCollectSubModels,
    MLReadable[TrainValidationSplit],
    MLWritable,
):
    def __init__(
        self,
        *,
        estimator: Optional[Estimator] = ...,
        estimatorParamMaps: Optional[List[ParamMap]] = ...,
        evaluator: Optional[Evaluator] = ...,
        trainRatio: float = ...,
        parallelism: int = ...,
        collectSubModels: bool = ...,
        seed: Optional[int] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        estimator: Optional[Estimator] = ...,
        estimatorParamMaps: Optional[List[ParamMap]] = ...,
        evaluator: Optional[Evaluator] = ...,
        trainRatio: float = ...,
        parallelism: int = ...,
        collectSubModels: bool = ...,
        seed: Optional[int] = ...
    ) -> TrainValidationSplit: ...
    def setEstimator(self, value: Estimator) -> TrainValidationSplit: ...
    def setEstimatorParamMaps(self, value: List[ParamMap]) -> TrainValidationSplit: ...
    def setEvaluator(self, value: Evaluator) -> TrainValidationSplit: ...
    def setTrainRatio(self, value: float) -> TrainValidationSplit: ...
    def setSeed(self, value: int) -> TrainValidationSplit: ...
    def setParallelism(self, value: int) -> TrainValidationSplit: ...
    def setCollectSubModels(self, value: bool) -> TrainValidationSplit: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> TrainValidationSplit: ...
    def write(self) -> MLWriter: ...
    @classmethod
    def read(cls: Type[TrainValidationSplit]) -> MLReader: ...

class TrainValidationSplitModel(
    Model,
    _TrainValidationSplitParams,
    MLReadable[TrainValidationSplitModel],
    MLWritable,
):
    bestModel: Model
    validationMetrics: List[float]
    subModels: List[Model]
    def __init__(
        self,
        bestModel: Model,
        validationMetrics: List[float] = ...,
        subModels: Optional[List[Model]] = ...,
    ) -> None: ...
    def setEstimator(self, value: Estimator) -> TrainValidationSplitModel: ...
    def setEstimatorParamMaps(
        self, value: List[ParamMap]
    ) -> TrainValidationSplitModel: ...
    def setEvaluator(self, value: Evaluator) -> TrainValidationSplitModel: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> TrainValidationSplitModel: ...
    def write(self) -> MLWriter: ...
    @classmethod
    def read(cls: Type[TrainValidationSplitModel]) -> MLReader: ...