<?php
// 隐藏报错
error_reporting(0);

// 设置默认返回格式
$on_data = array(
    'error' => false,
    'uuid' => '',
);
try {
    $conn = new mysqli("localhost", "账号", "密码", "库名");
} catch (PDOException $e) {
    $on_data = array(
        'error' => true,
        'msg' => '数据库连接失败',
    );
}

// 参数检查
if (!empty($_GET['admin'])) {
    $qq = $_GET['admin'];
    // 检查学校
    $getSchooData = $conn->prepare("SELECT * FROM schoolData WHERE qq = ?;");
    $getSchooData->bind_param("s", $qq);
    $getSchooData->execute();
    $result = $getSchooData->get_result();
    $schooData = $result->fetch_assoc();
    $getSchooData->close();
    // 检查管理员qq是否存在
    if (!$schooData) {
        $on_data = array(
            'error'=> true,
            'msg'=> "您的权限不足",
        );
        $conn->close();
        echo json_encode($on_data);
        exit();
    } else {
        $on_data['uuid'] = $schooData['uuid'];
        $conn->close();
        echo json_encode($on_data);
        exit();
    }
    
}

// 查询语句
$stmt = $conn->prepare("SELECT uuid FROM schoolData");
$stmt->execute();
$stmt->bind_result($uuid);
// 将结果转换为数组
$result = $stmt->get_result();
$data = $result->fetch_all(MYSQLI_ASSOC);
$values = array_column($data, 'uuid');

$stmt->close();
$conn->close();
$on_data['uuid'] = $values;
echo json_encode($on_data);
exit();