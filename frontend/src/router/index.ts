import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const SignalLight = () => import('@/views/signal_light/index.vue')
const SwitchMachine = () => import('@/views/switch_machine/index.vue')
const TrackCircuit = () => import('@/views/track_circuit/index.vue')
const Interlock = () => import('@/views/interlock/index.vue')
const AxleCounter = () => import('@/views/axle_counter/index.vue')
const PowerPanel = () => import('@/views/power_panel/index.vue')
const CableBox = () => import('@/views/cable_box/index.vue')
const Atp = () => import('@/views/atp/index.vue')
const Balise = () => import('@/views/balise/index.vue')
const InspectPlan = () => import('@/views/inspect_plan/index.vue')
const FaultRecord = () => import('@/views/fault_record/index.vue')
const Measure = () => import('@/views/measure/index.vue')
const SparePart = () => import('@/views/spare_part/index.vue')
const Tool = () => import('@/views/tool/index.vue')
const ShiftLog = () => import('@/views/shift_log/index.vue')
const TrainDetect = () => import('@/views/train_detect/index.vue')
const GroundEquip = () => import('@/views/ground_equip/index.vue')
const Tsr = () => import('@/views/tsr/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/signal_light', name: 'signal_light', component: SignalLight },
    { path: '/switch_machine', name: 'switch_machine', component: SwitchMachine },
    { path: '/track_circuit', name: 'track_circuit', component: TrackCircuit },
    { path: '/interlock', name: 'interlock', component: Interlock },
    { path: '/axle_counter', name: 'axle_counter', component: AxleCounter },
    { path: '/power_panel', name: 'power_panel', component: PowerPanel },
    { path: '/cable_box', name: 'cable_box', component: CableBox },
    { path: '/atp', name: 'atp', component: Atp },
    { path: '/balise', name: 'balise', component: Balise },
    { path: '/inspect_plan', name: 'inspect_plan', component: InspectPlan },
    { path: '/fault_record', name: 'fault_record', component: FaultRecord },
    { path: '/measure', name: 'measure', component: Measure },
    { path: '/spare_part', name: 'spare_part', component: SparePart },
    { path: '/tool', name: 'tool', component: Tool },
    { path: '/shift_log', name: 'shift_log', component: ShiftLog },
    { path: '/train_detect', name: 'train_detect', component: TrainDetect },
    { path: '/ground_equip', name: 'ground_equip', component: GroundEquip },
    { path: '/tsr', name: 'tsr', component: Tsr },
  ],
})

export default router
