# Machine Learning in Production Course: Homework 3
Maintainer: [Ruslan Akhmerov](https://data.mail.ru/profile/r.akhmerov/)

Status: in progress

## Project Roadmap

- [X] Установите kubectl

- [X] Разверните kubernetes  
    Вы можете развернуть его в облаке:
    - [ ] https://cloud.google.com/kubernetes-engine
    - [ ] https://mcs.mail.ru/containers/
    - [X] https://cloud.yandex.ru/services/managed-kubernetes
    Либо воспользоваться локальной инсталляцией
    - [ ] https://kind.sigs.k8s.io/docs/user/quick-start/
    - [ ] https://minikube.sigs.k8s.io/docs/start/
    Напишите, какой способ вы избрали.
- [X] Убедитесь, с кластер поднялся (kubectl cluster-info) 
(5 баллов)

- [X] Напишите простой pod manifests для вашего приложения, назовите его online-inference-pod.yaml (https://kubernetes.io/docs/concepts/workloads/pods/)
    - [X] Задеплойте приложение в кластер (kubectl apply -f online-inference-pod.yaml), убедитесь, что все поднялось (kubectl get pods)
    - [X] Приложите скриншот, где видно, что все поднялось
(4 балла)

- [X] Пропишите requests/limits и напишите зачем это нужно в описание PR
    - [X] закоммитьте файл online-inference-pod-resources.yaml
(2 балла)

- [X] Модифицируйте свое приложение так, чтобы оно стартовало не сразу(с задержкой секунд 20-30) и падало спустя минуты работы. 
Добавьте liveness и readiness пробы , посмотрите что будет происходить.
Напишите в описании -- чего вы этим добились.
Закоммититьте отдельный манифест online-inference-pod-probes.yaml (и изменение кода приложения)
    - [X] Опубликуйте ваше приложение(из ДЗ 2) с тэгом v2
(3 балла)

- [X] Создайте replicaset, сделайте 3 реплики вашего приложения. (https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
  - [X] Ответьте на вопрос, что будет, если сменить докер образа в манифесте и одновременно с этим 
    - [X] а) уменьшить число реплик
    - [X] б) увеличить число реплик.
    - [X] Поды с какими версиями образа будут внутри будут в кластере? 
  - [X] Закоммитьте online-inference-replicaset.yaml
(3 балла)

- [ ] Опишите деплоймент для вашего приложения.  (https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [ ] Играя с параметрами деплоя(maxSurge, maxUnavaliable), добейтесь ситуации, когда при деплое новой версии
    - [ ] a) Есть момент времени, когда на кластере есть как все старые поды, так и все новые (опишите эту ситуацию) (закоммититьте файл online-inference-deployment-blue-green.yaml)
    - [ ] б) одновременно с поднятием новых версии, гасятся старые (закоммитите файл online-inference-deployment-rolling-update.yaml)
(3 балла)

Бонусные активности:
- [ ] Установить helm и оформить helm chart, включить в состав чарта ConfigMap и Service.
(5 баллов)


## Самооценка
```
+ 0  За то, что я есть
+ 5  Поднял кластер и он поднялся. Триал GCP у меня уже исчерпан, потому Yandex.Cloud
+ 4  Написал простой манифест, всё завелось
+ 2  Прописал requests/limits
+ 3  Запушил версию 2 приложения, сделал liveness/readyness пробы
+ 0  Не делал replicaset
+ 0  Не описывал деплоймент
+ 0' Не имел дел с Helm
-------------------------------------------------------------------------------------
```
**ИТОГО: 14 / 20 базовых баллов + 0 / 5 дополнительных =** `14 / 25 баллов`