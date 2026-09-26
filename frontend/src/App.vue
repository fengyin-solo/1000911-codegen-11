<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">轨道交通信号设备检修管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">覆盖信号机、道岔转辙、轨道电路、联锁设备、计轴、电源屏及检修计划的轨道交通信号设备全生命周期管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "信号机管理", path: "/signal_light" }, { label: "道岔转辙机", path: "/switch_machine" }, { label: "轨道电路", path: "/track_circuit" }, { label: "联锁设备", path: "/interlock" }, { label: "计轴设备", path: "/axle_counter" }, { label: "信号电源屏", path: "/power_panel" }, { label: "电缆箱盒", path: "/cable_box" }, { label: "列控车载设备", path: "/atp" }, { label: "应答器管理", path: "/balise" }, { label: "检修计划", path: "/inspect_plan" }, { label: "故障记录", path: "/fault_record" }, { label: "电气特性测试", path: "/measure" }, { label: "备件管理", path: "/spare_part" }, { label: "工器具管理", path: "/tool" }, { label: "值班记录", path: "/shift_log" }, { label: "列车检测", path: "/train_detect" }, { label: "地面电子单元", path: "/ground_equip" }, { label: "临时限速", path: "/tsr" }]
</script>
