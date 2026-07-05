# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_18:14:57_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-07-05 18:14:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-05 18:14:57 UTC

- **130,230** saved flights
- **44,292** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **130,230** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,571,283.4 tonnes** estimated CO2 emissions
- **91,088,894 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5300 |
| 2 | SkyWest Airlines | 4821 |
| 3 | EJA | 2554 |
| 4 | IndiGo | 2443 |
| 5 | American Airlines | 2010 |
| 6 | Southwest Airlines | 1961 |
| 7 | ENY | 1637 |
| 8 | Delta Air Lines | 1563 |
| 9 | Lufthansa | 1367 |
| 10 | LATAM Airlines | 1187 |
| 11 | Vueling | 1154 |
| 12 | WIF | 1138 |
| 13 | AZU | 1107 |
| 14 | AXM | 1009 |
| 15 | LXJ | 1005 |
| 16 | Swiss International | 910 |
| 17 | All Nippon Airways | 860 |
| 18 | Alaska Airlines | 836 |
| 19 | easyJet | 834 |
| 20 | QLK | 816 |
| 21 | EJU | 804 |
| 22 | VIV | 722 |
| 23 | Cathay Pacific | 713 |
| 24 | AEE | 708 |
| 25 | Air France | 708 |
| 26 | CXK | 697 |
| 27 | United Airlines | 692 |
| 28 | JetBlue | 682 |
| 29 | MXY | 679 |
| 30 | GLO | 666 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 111483 |
| 2 | 🇪🇸 ES | 8688 |
| 3 | 🇮🇳 IN | 7653 |
| 4 | 🇦🇺 AU | 7519 |
| 5 | 🇧🇷 BR | 7321 |
| 6 | 🇨🇦 CA | 6869 |
| 7 | 🇩🇪 DE | 6844 |
| 8 | 🇮🇹 IT | 6803 |
| 9 | 🇬🇧 GB | 5792 |
| 10 | 🇯🇵 JP | 5624 |
| 11 | 🇫🇷 FR | 5182 |
| 12 | 🇨🇴 CO | 4102 |
| 13 | 🇲🇽 MX | 3805 |
| 14 | 🇬🇷 GR | 3717 |
| 15 | 🇳🇴 NO | 3537 |
| 16 | 🇨🇭 CH | 3349 |
| 17 | 🇹🇷 TR | 2868 |
| 18 | 🇲🇾 MY | 2616 |
| 19 | 🇿🇦 ZA | 2159 |
| 20 | 🇵🇱 PL | 2139 |
| 21 | 🇳🇿 NZ | 2080 |
| 22 | 🇹🇭 TH | 2014 |
| 23 | 🇰🇷 KR | 1963 |
| 24 | 🇵🇭 PH | 1813 |
| 25 | 🇬🇹 GT | 1773 |
| 26 | 🇲🇦 MA | 1391 |
| 27 | 🇲🇪 ME | 1294 |
| 28 | 🇳🇱 NL | 1225 |
| 29 | 🇲🇴 MO | 1186 |
| 30 | 🇭🇷 HR | 1144 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2717 |
| 2 | Denver International Airport |  | US | 2207 |
| 3 | Tokyo International Airport |  | JP | 1851 |
| 4 | Indira Gandhi International Airport |  | IN | 1689 |
| 5 | Harry Reid International Airport |  | US | 1617 |
| 6 | Guaymaral Airport |  | CO | 1587 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1539 |
| 8 | Zurich Airport |  | CH | 1437 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1387 |
| 10 | La Aurora Airport |  | GT | 1372 |
| 11 | Frankfurt am Main International Airport |  | DE | 1324 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1264 |
| 13 | Chicago O'Hare International Airport |  | US | 1251 |
| 14 | Macau International Airport |  | MO | 1186 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1157 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1104 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1073 |
| 19 | Madrid Barajas International Airport |  | ES | 1070 |
| 20 | Capua Airport |  | IT | 1067 |
| 21 | Congonhas Airport |  | BR | 1035 |
| 22 | Kuala Lumpur International Airport |  | MY | 1015 |
| 23 | Charlotte/Douglas International Airport |  | US | 972 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 950 |
| 25 | Charles de Gaulle International Airport |  | FR | 944 |
| 26 | Bengaluru International Airport |  | IN | 926 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 881 |
| 28 | Malpensa International Airport |  | IT | 878 |
| 29 | Ninoy Aquino International Airport |  | PH | 841 |
| 30 | Daniel K Inouye International Airport |  | US | 818 |
| 31 | Barcelona International Airport |  | ES | 808 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 795 |
| 33 | Tenerife Norte Airport |  | ES | 788 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 761 |
| 35 | Calgary International Airport |  | CA | 760 |
| 36 | Vitoria/Foronda Airport |  | ES | 750 |
| 37 | Seattle-Tacoma International Airport |  | US | 749 |
| 38 | Viracopos International Airport |  | BR | 746 |
| 39 | Scottsdale Airport |  | US | 746 |
| 40 | Amsterdam Airport Schiphol |  | NL | 741 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 666 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 471 | 21m | 244 km | 1,983.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 329 | 24m | 225 km | 1,276.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 327 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 315 | 1h 10m | 770 km | 4,184.5 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 247 | 26m | 275 km | 1,170.4 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 240 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 189 | 22m | 55 km | 179.6 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 183 | 44m | 241 km | 760.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 182 | 26m | 215 km | 674.1 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 179 | 20m | 99 km | 306.6 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 174 | 27m | 152 km | 454.7 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 169 | 1h 45m | 1,423 km | 4,147.5 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 163 | 31m | 369 km | 1,037.5 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 160 | 20m | 250 km | 691.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 160 | 18m | 144 km | 398.0 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 157 | 44m | 452 km | 1,223.6 t |
| 24 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 156 | 30m | 49 km | 131.9 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 154 | 1h 1m | 695 km | 1,846.0 t |
| 26 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 153 | 1h 16m | 961 km | 2,536.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 150 | 54m | 136 km | 351.6 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 148 | 1h 38m | 1,156 km | 2,952.5 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 145 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SDR11YL | SDR | Rayak Air Base (OLRA) | Ataturk International Airport (LTBA) | 2026-07-05 16:41 UTC | 2026-07-05 18:14 UTC | 1h 33m |
| N5473R |  | Mesquite Metro Airport (KHQZ) | Mesquite Metro Airport (KHQZ) | 2026-07-05 17:46 UTC | 2026-07-05 18:09 UTC | 22m |
| BPO160 | BPO | Bonn-Hangelar Airport (EDKB) | Bonn-Hangelar Airport (EDKB) | 2026-07-05 17:09 UTC | 2026-07-05 18:08 UTC | 59m |
| AMU949 | AMU | Kep Air Base (VVKP) | Macau International Airport (VMMC) | 2026-07-05 16:45 UTC | 2026-07-05 18:05 UTC | 1h 19m |
| N55291 |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-07-05 17:47 UTC | 2026-07-05 18:03 UTC | 15m |
| MNL14 | MNL | Truckee-Tahoe Airport (KTRK) | Norman Y Mineta San Jose International Airport (KSJC) | 2026-07-05 17:24 UTC | 2026-07-05 18:01 UTC | 36m |
| N58GX |  | Truckee-Tahoe Airport (KTRK) | San Carlos Airport (KSQL) | 2026-07-05 17:17 UTC | 2026-07-05 18:01 UTC | 44m |
| AAL2720 | American Airlines | St Louis Lambert International Airport (KSTL) | Philadelphia International Airport (KPHL) | 2026-07-05 16:16 UTC | 2026-07-05 18:00 UTC | 1h 44m |
| RWZ568 | RWZ | Batumi International Airport (UGSB) | Ben Gurion International Airport (LLBG) | 2026-07-05 10:39 UTC | 2026-07-05 18:00 UTC | 7h 21m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-07-05 16:44 UTC | 2026-07-05 17:59 UTC | 1h 14m |
| QTR9C | Qatar Airways | Munich International Airport (EDDM) | Queen Alia International Airport (OJAI) | 2026-07-05 15:05 UTC | 2026-07-05 17:58 UTC | 2h 53m |
| N124VA |  | Portsmouth International At Pease Airport (KPSM) | Skyhaven Airport (KDAW) | 2026-07-05 17:49 UTC | 2026-07-05 17:58 UTC | 8m |
| N139BG |  | 0PA0 (0PA0) | 0PA0 (0PA0) | 2026-07-05 17:40 UTC | 2026-07-05 17:57 UTC | 17m |
| N5518W |  | Neversweat Airport (1OK0) | Double W Airport (3OK7) | 2026-07-05 17:22 UTC | 2026-07-05 17:57 UTC | 35m |
| KAL9231 | Korean Air | Ted Stevens Anchorage International Airport (PANC) | Dawson Creek Airport (CYDQ) | 2026-07-05 15:51 UTC | 2026-07-05 17:57 UTC | 2h 5m |
| KNE842 | KNE | Trabzon International Airport (LTCG) | Khurais Airport (OEKR) | 2026-07-05 15:02 UTC | 2026-07-05 17:56 UTC | 2h 54m |
| XSN06 | XSN | Bodad Airport (CA11) | San Carlos Airport (KSQL) | 2026-07-05 16:50 UTC | 2026-07-05 17:55 UTC | 1h 5m |
| N36HF |  | Newark Liberty International Airport (KEWR) | Francis S Gabreski Airport (KFOK) | 2026-07-05 17:11 UTC | 2026-07-05 17:54 UTC | 42m |
| N756DN |  | Brown Field Municipal Airport (KSDM) | Brown Field Municipal Airport (KSDM) | 2026-07-05 17:35 UTC | 2026-07-05 17:54 UTC | 18m |
| N405SB |  | K5M3 (K5M3) | Laconia Municipal Airport (KLCI) | 2026-07-05 17:38 UTC | 2026-07-05 17:52 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
