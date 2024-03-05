import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings('ignore')

# 1. 데이터
x, y = load_digits(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=777, train_size=0.8)

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# parameters = {
    
    
# }
parameters = {
    # 'objective': 'binary:logistic',  # 분류 문제인 경우 이진 분류를 위해 'binary:logistic'으로 설정합니다.
    # 'eval_metric': 'logloss',  # 모델 평가 지표로 로그 손실을 사용합니다.
    'max_depth': 6,  # 트리의 최대 깊이를 설정합니다.
    'learning_rate': 0.1,  # 학습률을 설정합니다.
    'n_estimators': 100,  # 트리의 개수를 설정합니다.
    'subsample': 0.8,  # 각 트리마다 사용될 샘플의 비율을 설정합니다.
    'colsample_bytree': 0.8,  # 각 트리마다 사용될 피처의 비율을 설정합니다.
    'reg_alpha': 0,  # L1 정규화 파라미터를 설정합니다.
    'reg_lambda': 1,  # L2 정규화 파라미터를 설정합니다.
    'random_state': 42  # 랜덤 시드를 설정합니다.
}

# 2. 모델

model = XGBClassifier()
model.set_params(early_stopping_rounds=10, **parameters)

# 3. 훈련
model.fit(x_train, y_train,
          eval_set=[(x_train, y_train), (x_test, y_test)],
          verbose=1,
          eval_metric='mlogloss'
          )

# 4. 평가, 예측
results = model.score(x_test, y_test)
print("최종 점수 : ", results)

y_predict = model.predict(x_test)
acc = accuracy_score(y_test, y_predict)
print("acc_score : ", acc)

###############################################################
print("------------------------------------------------------------")
# print(model.feature_importances_)
feature_importances = model.feature_importances_

print(feature_importances)
# print(x_train.shape)    #(455, 30) 

num_iterations = x_train.shape[1] - 1

for i in range(num_iterations) :
    
    feature_importances =  model.feature_importances_
    min_importance_index = np.argmin(feature_importances)
    min_importance = feature_importances[min_importance_index]
    
    x_train = np.delete(x_train, min_importance_index, axis=1)
    x_test = np.delete(x_test, min_importance_index, axis=1)

    print(x_train.shape, x_test.shape)
    
    model = XGBClassifier()
    model.set_params(early_stopping_rounds=10, **parameters)
    
    model.fit(x_train, y_train,
          eval_set=[(x_train, y_train), (x_test, y_test)],
          verbose=0,
          eval_metric='mlogloss'
          )
    
    # 4. 평가
    results = model.score(x_test, y_test)
    # print("최종 점수 : ", results)

    y_predict = model.predict(x_test)
    acc = accuracy_score(y_test, y_predict)
    # print("acc_score : ", acc)
    print(f"acc : {acc}")
    print(f"제거된 특성 {min_importance_index}의 중요도 : {min_importance}")
    print("-----------------------------------------------------------------------")
    
#     (1437, 63) (360, 63)
# acc : 0.9694444444444444
# 제거된 특성 0의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 62) (360, 62)
# acc : 0.9666666666666667
# 제거된 특성 7의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 61) (360, 61)
# acc : 0.9722222222222222
# 제거된 특성 14의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 60) (360, 60)
# acc : 0.9666666666666667
# 제거된 특성 21의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 59) (360, 59)
# acc : 0.9638888888888889
# 제거된 특성 27의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 58) (360, 58)
# acc : 0.9666666666666667
# 제거된 특성 27의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 57) (360, 57)
# acc : 0.9722222222222222
# 제거된 특성 33의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 56) (360, 56)
# acc : 0.9694444444444444
# 제거된 특성 33의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 55) (360, 55)
# acc : 0.9666666666666667
# 제거된 특성 39의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 54) (360, 54)
# acc : 0.9694444444444444
# 제거된 특성 39의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 53) (360, 53)
# acc : 0.9638888888888889
# 제거된 특성 46의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 52) (360, 52)
# acc : 0.9638888888888889
# 제거된 특성 46의 중요도 : 0.0029906206764280796
# -----------------------------------------------------------------------
# (1437, 51) (360, 51)
# acc : 0.9722222222222222
# 제거된 특성 39의 중요도 : 0.003973798360675573
# -----------------------------------------------------------------------
# (1437, 50) (360, 50)
# acc : 0.9722222222222222
# 제거된 특성 44의 중요도 : 0.00260278582572937
# -----------------------------------------------------------------------
# (1437, 49) (360, 49)
# acc : 0.9694444444444444
# 제거된 특성 20의 중요도 : 0.0
# -----------------------------------------------------------------------
# (1437, 48) (360, 48)
# acc : 0.9666666666666667
# 제거된 특성 9의 중요도 : 0.004843960981816053
# -----------------------------------------------------------------------
# (1437, 47) (360, 47)
# acc : 0.9666666666666667
# 제거된 특성 43의 중요도 : 0.00525263138115406
# -----------------------------------------------------------------------
# (1437, 46) (360, 46)
# acc : 0.9611111111111111
# 제거된 특성 13의 중요도 : 0.005384460091590881
# -----------------------------------------------------------------------
# (1437, 45) (360, 45)
# acc : 0.9638888888888889
# 제거된 특성 18의 중요도 : 0.005532483570277691
# -----------------------------------------------------------------------
# (1437, 44) (360, 44)
# acc : 0.9638888888888889
# 제거된 특성 11의 중요도 : 0.006267559248954058
# -----------------------------------------------------------------------
# (1437, 43) (360, 43)
# acc : 0.9694444444444444
# 제거된 특성 3의 중요도 : 0.007440303917974234
# -----------------------------------------------------------------------
# (1437, 42) (360, 42)
# acc : 0.9638888888888889
# 제거된 특성 15의 중요도 : 0.0062668840400874615
# -----------------------------------------------------------------------
# (1437, 41) (360, 41)
# acc : 0.9694444444444444
# 제거된 특성 34의 중요도 : 0.006517565809190273
# -----------------------------------------------------------------------
# (1437, 40) (360, 40)
# acc : 0.9694444444444444
# 제거된 특성 8의 중요도 : 0.008814163506031036
# -----------------------------------------------------------------------
# (1437, 39) (360, 39)
# acc : 0.9666666666666667
# 제거된 특성 6의 중요도 : 0.007563954219222069
# -----------------------------------------------------------------------
# (1437, 38) (360, 38)
# acc : 0.9638888888888889
# 제거된 특성 9의 중요도 : 0.009540309198200703
# -----------------------------------------------------------------------
# (1437, 37) (360, 37)
# acc : 0.9583333333333334
# 제거된 특성 0의 중요도 : 0.009009400382637978
# -----------------------------------------------------------------------
# (1437, 36) (360, 36)
# acc : 0.9583333333333334
# 제거된 특성 22의 중요도 : 0.010051901452243328
# -----------------------------------------------------------------------
# (1437, 35) (360, 35)
# acc : 0.9611111111111111
# 제거된 특성 1의 중요도 : 0.011397367343306541
# -----------------------------------------------------------------------
# (1437, 34) (360, 34)
# acc : 0.9638888888888889
# 제거된 특성 17의 중요도 : 0.010616263374686241
# -----------------------------------------------------------------------
# (1437, 33) (360, 33)
# acc : 0.9611111111111111
# 제거된 특성 25의 중요도 : 0.00788914319127798
# -----------------------------------------------------------------------
# (1437, 32) (360, 32)
# acc : 0.9666666666666667
# 제거된 특성 2의 중요도 : 0.01228510495275259
# -----------------------------------------------------------------------
# (1437, 31) (360, 31)
# acc : 0.9611111111111111
# 제거된 특성 21의 중요도 : 0.01538905967026949
# -----------------------------------------------------------------------
# (1437, 30) (360, 30)
# acc : 0.9555555555555556
# 제거된 특성 23의 중요도 : 0.015530258417129517
# -----------------------------------------------------------------------
# (1437, 29) (360, 29)
# acc : 0.9527777777777777
# 제거된 특성 15의 중요도 : 0.01254233904182911
# -----------------------------------------------------------------------
# (1437, 28) (360, 28)
# acc : 0.9555555555555556
# 제거된 특성 10의 중요도 : 0.01711713708937168
# -----------------------------------------------------------------------
# (1437, 27) (360, 27)
# acc : 0.9583333333333334
# 제거된 특성 5의 중요도 : 0.01648748107254505
# -----------------------------------------------------------------------
# (1437, 26) (360, 26)
# acc : 0.9555555555555556
# 제거된 특성 0의 중요도 : 0.017575712874531746
# -----------------------------------------------------------------------
# (1437, 25) (360, 25)
# acc : 0.9611111111111111
# 제거된 특성 5의 중요도 : 0.024137668311595917
# -----------------------------------------------------------------------
# (1437, 24) (360, 24)
# acc : 0.95
# 제거된 특성 16의 중요도 : 0.01874944008886814
# -----------------------------------------------------------------------
# (1437, 23) (360, 23)
# acc : 0.9472222222222222
# 제거된 특성 2의 중요도 : 0.021894363686442375
# -----------------------------------------------------------------------
# (1437, 22) (360, 22)
# acc : 0.9527777777777777
# 제거된 특성 11의 중요도 : 0.024672923609614372
# -----------------------------------------------------------------------
# (1437, 21) (360, 21)
# acc : 0.9472222222222222
# 제거된 특성 19의 중요도 : 0.02088814787566662
# -----------------------------------------------------------------------
# (1437, 20) (360, 20)
# acc : 0.9472222222222222
# 제거된 특성 8의 중요도 : 0.030436983332037926
# -----------------------------------------------------------------------
# (1437, 19) (360, 19)
# acc : 0.9472222222222222
# 제거된 특성 19의 중요도 : 0.028830446302890778
# -----------------------------------------------------------------------
# (1437, 18) (360, 18)
# acc : 0.9472222222222222
# 제거된 특성 0의 중요도 : 0.035870157182216644
# -----------------------------------------------------------------------
# (1437, 17) (360, 17)
# acc : 0.9416666666666667
# 제거된 특성 15의 중요도 : 0.03604889661073685
# -----------------------------------------------------------------------
# (1437, 16) (360, 16)
# acc : 0.9416666666666667
# 제거된 특성 13의 중요도 : 0.03773912414908409
# -----------------------------------------------------------------------
# (1437, 15) (360, 15)
# acc : 0.9333333333333333
# 제거된 특성 6의 중요도 : 0.036892522126436234
# -----------------------------------------------------------------------
# (1437, 14) (360, 14)
# acc : 0.9416666666666667
# 제거된 특성 1의 중요도 : 0.04445568472146988
# -----------------------------------------------------------------------
# (1437, 13) (360, 13)
# acc : 0.9361111111111111
# 제거된 특성 4의 중요도 : 0.041451241821050644
# -----------------------------------------------------------------------
# (1437, 12) (360, 12)
# acc : 0.9222222222222223
# 제거된 특성 11의 중요도 : 0.05622509866952896
# -----------------------------------------------------------------------
# (1437, 11) (360, 11)
# acc : 0.9
# 제거된 특성 1의 중요도 : 0.059276826679706573
# -----------------------------------------------------------------------
# (1437, 10) (360, 10)
# acc : 0.8944444444444445
# 제거된 특성 8의 중요도 : 0.07273862510919571
# -----------------------------------------------------------------------
# (1437, 9) (360, 9)
# acc : 0.8972222222222223
# 제거된 특성 0의 중요도 : 0.08499796688556671
# -----------------------------------------------------------------------
# (1437, 8) (360, 8)
# acc : 0.8833333333333333
# 제거된 특성 3의 중요도 : 0.09518927335739136
# -----------------------------------------------------------------------
# (1437, 7) (360, 7)
# acc : 0.8472222222222222
# 제거된 특성 6의 중요도 : 0.10247024893760681
# -----------------------------------------------------------------------
# (1437, 6) (360, 6)
# acc : 0.775
# 제거된 특성 1의 중요도 : 0.11634863913059235
# -----------------------------------------------------------------------
# (1437, 5) (360, 5)
# acc : 0.7388888888888889
# 제거된 특성 3의 중요도 : 0.14779981970787048
# -----------------------------------------------------------------------
# (1437, 4) (360, 4)
# acc : 0.5944444444444444
# 제거된 특성 3의 중요도 : 0.1797601878643036
# -----------------------------------------------------------------------
# (1437, 3) (360, 3)
# acc : 0.5055555555555555
# 제거된 특성 2의 중요도 : 0.23443470895290375
# -----------------------------------------------------------------------
# (1437, 2) (360, 2)
# acc : 0.37777777777777777
# 제거된 특성 2의 중요도 : 0.29156777262687683
# -----------------------------------------------------------------------
# (1437, 1) (360, 1)
# acc : 0.2388888888888889
# 제거된 특성 0의 중요도 : 0.41549167037010193
# -----------------------------------------------------------------------