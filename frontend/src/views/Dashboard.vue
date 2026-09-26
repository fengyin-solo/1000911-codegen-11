<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "信号机管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "道岔转辙机", "created": 0, "pending": 0, "abnormal": 0}, {"name": "轨道电路", "created": 0, "pending": 0, "abnormal": 0}, {"name": "联锁设备", "created": 0, "pending": 0, "abnormal": 0}, {"name": "计轴设备", "created": 0, "pending": 0, "abnormal": 0}, {"name": "信号电源屏", "created": 0, "pending": 0, "abnormal": 0}, {"name": "电缆箱盒", "created": 0, "pending": 0, "abnormal": 0}, {"name": "列控车载设备", "created": 0, "pending": 0, "abnormal": 0}, {"name": "应答器管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "检修计划", "created": 0, "pending": 0, "abnormal": 0}, {"name": "故障记录", "created": 0, "pending": 0, "abnormal": 0}, {"name": "电气特性测试", "created": 0, "pending": 0, "abnormal": 0}, {"name": "备件管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "工器具管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "值班记录", "created": 0, "pending": 0, "abnormal": 0}, {"name": "列车检测", "created": 0, "pending": 0, "abnormal": 0}, {"name": "地面电子单元", "created": 0, "pending": 0, "abnormal": 0}, {"name": "临时限速", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
