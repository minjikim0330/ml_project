[reference_analysis.md](https://github.com/user-attachments/files/26198528/reference_analysis.md)
# 1) 데이터셋 분석

심장질환 예측을 위해 UCI 기반의 의료 데이터를 활용하였다.

-   270명의 환자
-   14개의 변수 (13 feature + 1 target)

## 변수 구성

-   수치형: age, trestbps, chol, thalach, oldpeck
-   범주형: sex, cp, fbs, restecg, exang, slope, ca, thal

## 데이터 전처리

-   결측치 없음
-   추가적인 피처 엔지니어링 없음
-   StandardScaler를 사용하여 평균 0, 표준편차 1로 정규화
-   학습 데이터로만 fit 후 테스트 데이터에 transform 적용 (데이터 누수
    방지)

------------------------------------------------------------------------

# 2) 모델링 분석

## 사용 알고리즘

-   Logistic Regression
-   Decision Tree
-   Random Forest
-   Gradient Boosting
-   K-Nearest Neighbors (KNN)
-   Support Vector Machine (SVM, RBF kernel)
-   Naive Bayes

## 알고리즘 선택 이유

-   Logistic Regression: 해석이 쉬운 기본 선형 모델
-   Decision Tree: 직관적인 규칙 기반 모델
-   Random Forest: 과적합 감소 및 성능 향상
-   Gradient Boosting: 오차를 보완하며 학습하는 고성능 모델
-   KNN: 거리 기반 분류 모델
-   SVM: 복잡한 결정 경계 학습 가능
-   Naive Bayes: 빠르고 단순한 확률 기반 모델

------------------------------------------------------------------------

# 3) 성능 평가 분석

## 평가 지표

-   Accuracy
-   Precision
-   Recall
-   F1-score
-   ROC-AUC
-   Cross Validation Mean / Std

## 성능 결과

-   Logistic Regression과 Naive Bayes가 약 87% 정확도로 가장 우수
-   Logistic Regression:
    -   Accuracy: 0.8704
    -   F1-score: 0.8627
    -   ROC-AUC: 0.9097

## 해석

-   대부분 모델이 유사한 성능을 보임
-   데이터가 잘 정제되어 있으며 특정 모델 의존도가 낮음
