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

- [ ] Напишите простой pod manifests для вашего приложения, назовите его online-inference-pod.yaml (https://kubernetes.io/docs/concepts/workloads/pods/)
    - [ ] Задеплойте приложение в кластер (kubectl apply -f online-inference-pod.yaml), убедитесь, что все поднялось (kubectl get pods)
    - [ ] Приложите скриншот, где видно, что все поднялось
(4 балла)

- [ ] Пропишите requests/limits и напишите зачем это нужно в описание PR
    - [ ] закоммитьте файл online-inference-pod-resources.yaml
(2 балла)

- [ ] Модифицируйте свое приложение так, чтобы оно стартовало не сразу(с задержкой секунд 20-30) и падало спустя минуты работы. 
Добавьте liveness и readiness пробы , посмотрите что будет происходить.
Напишите в описании -- чего вы этим добились.
Закоммититьте отдельный манифест online-inference-pod-probes.yaml (и изменение кода приложения)
(3 балла)

- [ ] Опубликуйте ваше приложение(из ДЗ 2) с тэгом v2
  - [ ] Создайте replicaset, сделайте 3 реплики вашего приложения. (https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
  - [ ] Ответьте на вопрос, что будет, если сменить докер образа в манифесте и одновременно с этим 
        - [ ] а) уменьшить число реплик
        - [ ] б) увеличить число реплик.
        - [ ] Поды с какими версиями образа будут внутри будут в кластере? 
  - [ ]Закоммитьте online-inference-replicaset.yaml
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
TODO