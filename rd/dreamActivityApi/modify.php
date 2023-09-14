<?php
// 隐藏报错
error_reporting(0);

// 参数检查
if (empty($_GET['admin'])) {
  $on_data = array(
    'error' => true,
    'msg' => '缺少参数，admin',
  );
  echo json_encode($on_data);
  exit();
}

// 设置默认返回格式
$on_data = array(
    'error' => false,
    'msg' => '',
);
try {
    $conn = new mysqli("localhost", "账号", "密码", "库名");
} catch (PDOException $e) {
    $on_data = array(
        'error' => true,
        'msg' => '数据库连接失败',
    );
}
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
} 

$id = $schooData['id'];

// 参数检查1
if (!empty($_GET['close'])) {
    if ($schooData['open'] == 1) {
        $open = 0;
        $on_data['msg'] = '监测已开启';
    } else {
        $open = 1;
        $on_data['msg'] = '监测已关闭';
    }
    $stmt = $conn->prepare("UPDATE schoolData SET open = ? WHERE id = ?");
    $stmt->bind_param('ii', $open, $id);
    $stmt->execute();
    $stmt->close();
    $conn->close();
    echo json_encode($on_data);
    exit();
}
// 参数检查2
if (!empty($_GET['d'])) {
    $d = $_GET['d'];
    $stmt = $conn->prepare("UPDATE schoolData SET d = ?, ban = 0 WHERE id = ?");
    $stmt->bind_param('si', $d, $id);
    $stmt->execute();
    $stmt->close();
    $conn->close();
    $on_data['msg'] = '更新成功';
    echo json_encode($on_data);
    exit();
}
$on_data['error'] = true;
$on_data['msg'] = '还至少需要一种参数close或d';
echo json_encode($on_data);
exit();