glance list
| 4e6ddfd9-8b0f-4d5c-b7f8-ab0812b2dbcf | Official_Ubuntu_14.04.1_amd64_linux-image-3.13.0-32-generic | qcow2       | bare             | 255066624   | active |
| b8f85c7a-a5fa-477c-b446-259336dc83d5 | shihta-ms0                                                  | qcow2       | bare             | 1366884352  | active |
| 666f6dcf-590f-4e2c-b650-73da2d7de7e6 | shihta-ms1                                                  | qcow2       | bare             | 4733075456  | active |
nova flavor-list
+----+-----------+-----------+------+-----------+------+-------+-------------+-----------+
| ID | Name      | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
+----+-----------+-----------+------+-----------+------+-------+-------------+-----------+
| 1  | m1.tiny   | 512       | 0    | 0         |      | 1     | 1.0         | True      |
| 2  | m1.small  | 2048      | 50   | 0         |      | 1     | 1.0         | True      |
| 3  | m1.medium | 4096      | 100  | 0         |      | 2     | 1.0         | True      |
| 4  | m1.large  | 8192      | 150  | 0         |      | 4     | 1.0         | True      |
| 5  | m1.xlarge | 16384     | 250  | 0         |      | 8     | 1.0         | True      |
| 6  | c1.tiny   | 512       | 0    | 0         |      | 2     | 1.0         | True      |
| 7  | c1.small  | 2048      | 25   | 0         |      | 4     | 1.0         | True      |
| 8  | c1.medium | 4096      | 50   | 0         |      | 8     | 1.0         | True      |
+----+-----------+-----------+------+-----------+------+-------+-------------+-----------+
nova secgroup-list
+--------------------------------------+--------------+----------------------------------+
| Id                                   | Name         | Description                      |
+--------------------------------------+--------------+----------------------------------+
| 48115b39-1915-4501-b605-a4e25ad3e941 | 12312port    | 12312port                        |
| cbf9d3f5-31f8-4c19-a94e-821e9dbd8e77 | aio          | all                              |
| 7f419ed2-a572-4cea-aa4e-d304dbefb551 | cloudera     | 7180port                         |
| 8c1ad899-a6dc-4fd7-ae86-3840dd7ff17e | default      | default                          |
| d97b8d83-833d-491f-a758-d08f93ee90ed | hadoop       | 9000 and 9001                    |
| 410c5a5d-3c90-4aa4-909a-ce87b8ad9a35 | hive         | 9083                             |
| 365d4eb9-4cb0-49c2-ab71-96a36e4cab1e | http         | how about allowing http ingress? |
| 2e880397-2fe9-4322-bc06-9bbed34a179b | http_node    | nodejs testing by laman          |
| e46ccf6f-b640-41e9-b237-8b998ff5e447 | mongodb      | port 27017, 28017                |
| 635719d1-7b37-44f8-b801-3ca4d79f90e7 | mysql-3306   | 3306 port                        |
| 9118969b-d5d2-44ed-aa64-6c1550d0c315 | postgresql   | port:5432                        |
| 14d6e553-f399-46e0-accf-8158cd183757 | scm          | 7182                             |
| 92420e0c-c472-4de5-894f-deb1eaab71fc | solr         | 8983                             |
| 52991648-6883-4ed2-bfca-a93bb0aa5ac6 | taco-service | allow taco service               |
+--------------------------------------+--------------+----------------------------------+
nova keypair-list
+-------------+-------------------------------------------------+
| Name        | Fingerprint                                     |
+-------------+-------------------------------------------------+
| kuster_DQ45 | dc:a0:55:7d:cf:4a:b1:18:66:10:8a:fc:4b:e4:88:b7 |
| MBA         | a6:87:51:01:6d:4e:f8:75:dc:96:4a:06:1b:1d:98:cd |
| root_DQ45   | 6d:e6:5d:78:93:4f:d8:6e:95:7b:7e:0b:a6:00:c2:4a |
+-------------+-------------------------------------------------+

nova boot --image <image> --flavor <flavor> --key-name <key-name> --nic net-id=<net-uuid> <name>
nova boot --image 4e6ddfd9-8b0f-4d5c-b7f8-ab0812b2dbcf --flavor c1.medium --key-name MBA shihta-swift-00
nova boot --image 4e6ddfd9-8b0f-4d5c-b7f8-ab0812b2dbcf --flavor c1.medium --key-name MBA --availability-zone services shihta-swift-01 >> ERROR
nova add-secgroup shihta-swift-00 12312port
nova list-secgroup shihta-swift-00






