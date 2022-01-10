import { Space, Table, Tag } from "antd";
import { useQuery } from "react-query";

export default function ProfessorsTable() {
  const { isLoading, error, data } = useQuery("repoData", () =>
    fetch("http://localhost:8000/api/professors").then((res) => res.json())
  );

  console.log(data);

  const columns = [
    { title: "Full name", dataIndex: "full_name", key: "full_name" },
    { title: "Email", dataIndex: "email", key: "full_name" },
    {
      title: "Status",
      dataIndex: "is_active",
      key: "is_active",
      render: (is_active: boolean) => {
        console.log(is_active);
        let color = is_active ? "geekblue" : "volcano";
        let status = is_active ? "Logged in" : "Pending Invite";
        return <Tag color={color}>{status}</Tag>;
      },
    },
    {
      title: "Action",
      key: "action",
      render: (text, record) => (
        <Space size="middle">
          <a>Edit</a>
          <a>Delete</a>
        </Space>
      ),
    },
  ];

  return (
    <Table
      dataSource={data}
      columns={columns}
      loading={isLoading}
      rowKey="professor_id"
      showSorterTooltip
      sticky
    >
      Button
    </Table>
  );
}
