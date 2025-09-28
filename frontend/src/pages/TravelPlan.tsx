import React, { useState } from "react";
import {
  Box,
  Drawer,
  Typography,
  List,
  ListItem,
  Button,
  Modal,
  TextField,
  Grid,
} from "@mui/material";
import { MapContainer, TileLayer } from "react-leaflet";

interface Plan {
  name: string;
  city: string;
}

export default function TravelMapPage() {
  const [plans, setPlans] = useState<Plan[]>([
    { name: "云南之旅", city: "昆明" },
    { name: "北京文化游", city: "北京" },
  ]);
  const [openModal, setOpenModal] = useState(false);
  const [newPlan, setNewPlan] = useState<Plan>({ name: "", city: "" });

  const addPlan = () => {
    if (newPlan.name && newPlan.city) {
      setPlans([...plans, { ...newPlan }]);
      setNewPlan({ name: "", city: "" });
      setOpenModal(false);
    }
  };

  return (
    <Box sx={{ display: "flex", height: "100vh" }}>
      {/* 左侧栏 */}
      <Drawer
        variant="permanent"
        anchor="left"
        sx={{
          width: 300,
          flexShrink: 0,
          "& .MuiDrawer-paper": { width: 300, boxSizing: "border-box" },
        }}
      >
        <Box sx={{ p: 2 }}>
          <Typography variant="h6">旅行计划</Typography>

          {/* 上半部分：已有计划列表 */}
          <List>
            {plans.map((plan, index) => (
              <ListItem key={index}>{plan.name}</ListItem>
            ))}
          </List>

          {/* 下半部分：按钮 */}
          <Box sx={{ mt: 4 }}>
            <Button
              fullWidth
              variant="contained"
              sx={{ mb: 2 }}
              onClick={() => setOpenModal(true)}
            >
              New Plan
            </Button>
            <Grid container spacing={1}>
              <Grid item xs={6}>
                <Button fullWidth variant="outlined">
                  设置
                </Button>
              </Grid>
              <Grid item xs={6}>
                <Button fullWidth variant="outlined">
                  关于
                </Button>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Drawer>

      {/* 右侧地图 */}
      <Box sx={{ flexGrow: 1 }}>
        <MapContainer center={[20, 0]} zoom={2} style={{ height: "100%" }}>
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        </MapContainer>
      </Box>

      {/* 新建计划弹窗 */}
      <Modal open={openModal} onClose={() => setOpenModal(false)}>
        <Box
          sx={{
            position: "absolute" as "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            width: 300,
            bgcolor: "background.paper",
            boxShadow: 24,
            p: 4,
          }}
        >
          <Typography variant="h6" sx={{ mb: 2 }}>
            新建计划
          </Typography>
          <TextField
            fullWidth
            label="计划名称"
            sx={{ mb: 2 }}
            value={newPlan.name}
            onChange={(e) => setNewPlan({ ...newPlan, name: e.target.value })}
          />
          <TextField
            fullWidth
            label="城市"
            sx={{ mb: 2 }}
            value={newPlan.city}
            onChange={(e) => setNewPlan({ ...newPlan, city: e.target.value })}
          />
          <Button fullWidth variant="contained" onClick={addPlan}>
            添加
          </Button>
        </Box>
      </Modal>
    </Box>
  );
}
