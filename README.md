# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_20:09:55_UTC-green)

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

**Latest saved flight:** 2026-06-14 20:09:55 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-14 20:09:55 UTC

- **110,668** saved flights
- **38,600** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **110,668** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,353,280.5 tonnes** estimated CO2 emissions
- **78,451,044 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4575 |
| 2 | SkyWest Airlines | 4132 |
| 3 | IndiGo | 2173 |
| 4 | EJA | 2139 |
| 5 | American Airlines | 1745 |
| 6 | Southwest Airlines | 1657 |
| 7 | ENY | 1375 |
| 8 | Delta Air Lines | 1304 |
| 9 | Lufthansa | 1254 |
| 10 | Vueling | 1017 |
| 11 | LATAM Airlines | 978 |
| 12 | WIF | 978 |
| 13 | AXM | 933 |
| 14 | AZU | 916 |
| 15 | LXJ | 840 |
| 16 | Swiss International | 795 |
| 17 | All Nippon Airways | 769 |
| 18 | Alaska Airlines | 752 |
| 19 | QLK | 726 |
| 20 | easyJet | 711 |
| 21 | EJU | 706 |
| 22 | Cathay Pacific | 657 |
| 23 | AEE | 628 |
| 24 | VIV | 622 |
| 25 | Air France | 621 |
| 26 | United Airlines | 612 |
| 27 | MXY | 592 |
| 28 | CXK | 578 |
| 29 | AXB | 546 |
| 30 | Japan Airlines | 542 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 93036 |
| 2 | 🇪🇸 ES | 7604 |
| 3 | 🇮🇳 IN | 6852 |
| 4 | 🇦🇺 AU | 6569 |
| 5 | 🇧🇷 BR | 6110 |
| 6 | 🇮🇹 IT | 5975 |
| 7 | 🇩🇪 DE | 5937 |
| 8 | 🇨🇦 CA | 5793 |
| 9 | 🇯🇵 JP | 5015 |
| 10 | 🇬🇧 GB | 4747 |
| 11 | 🇫🇷 FR | 4433 |
| 12 | 🇨🇴 CO | 3763 |
| 13 | 🇲🇽 MX | 3286 |
| 14 | 🇬🇷 GR | 3154 |
| 15 | 🇳🇴 NO | 3069 |
| 16 | 🇨🇭 CH | 2834 |
| 17 | 🇲🇾 MY | 2409 |
| 18 | 🇹🇷 TR | 2197 |
| 19 | 🇿🇦 ZA | 1887 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1826 |
| 22 | 🇵🇱 PL | 1821 |
| 23 | 🇳🇿 NZ | 1807 |
| 24 | 🇵🇭 PH | 1611 |
| 25 | 🇬🇹 GT | 1579 |
| 26 | 🇲🇦 MA | 1218 |
| 27 | 🇲🇴 MO | 1150 |
| 28 | 🇲🇪 ME | 1085 |
| 29 | 🇳🇱 NL | 1083 |
| 30 | 🇭🇷 HR | 962 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2362 |
| 2 | Denver International Airport |  | US | 1871 |
| 3 | Tokyo International Airport |  | JP | 1661 |
| 4 | Indira Gandhi International Airport |  | IN | 1491 |
| 5 | Guaymaral Airport |  | CO | 1397 |
| 6 | Harry Reid International Airport |  | US | 1394 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1380 |
| 8 | Zurich Airport |  | CH | 1246 |
| 9 | Frankfurt am Main International Airport |  | DE | 1229 |
| 10 | La Aurora Airport |  | GT | 1215 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1185 |
| 12 | Macau International Airport |  | MO | 1150 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1105 |
| 15 | Chicago O'Hare International Airport |  | US | 1096 |
| 16 | Madrid Barajas International Airport |  | ES | 969 |
| 17 | Capua Airport |  | IT | 963 |
| 18 | Kuala Lumpur International Airport |  | MY | 940 |
| 19 | Salt Lake City International Airport |  | US | 935 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 934 |
| 21 | Charlotte/Douglas International Airport |  | US | 851 |
| 22 | Congonhas Airport |  | BR | 850 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 833 |
| 24 | Charles de Gaulle International Airport |  | FR | 832 |
| 25 | Bengaluru International Airport |  | IN | 828 |
| 26 | Malpensa International Airport |  | IT | 809 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 749 |
| 28 | Ninoy Aquino International Airport |  | PH | 742 |
| 29 | Daniel K Inouye International Airport |  | US | 736 |
| 30 | Tenerife Norte Airport |  | ES | 731 |
| 31 | Barcelona International Airport |  | ES | 726 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 722 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 708 |
| 34 | Don Mueang International Airport |  | TH | 667 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 658 |
| 37 | Calgary International Airport |  | CA | 651 |
| 38 | Seattle-Tacoma International Airport |  | US | 633 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 632 |
| 40 | Viracopos International Airport |  | BR | 624 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 579 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 404 | 21m | 244 km | 1,701.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 286 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 271 | 1h 25m | 910 km | 4,252.6 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 260 | 1h 10m | 770 km | 3,453.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 221 | 26m | 275 km | 1,047.2 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 164 | 20m | 99 km | 280.9 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 161 | 27m | 215 km | 596.3 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 157 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 149 | 31m | 369 km | 948.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 140 | 44m | 241 km | 581.5 t |
| 24 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 124 | 12m | - | - |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 123 | 24m | 223 km | 473.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EXS64KM | EXS | Manchester Airport (EGCC) | Luqa Airport (LMML) | 2026-06-14 17:13 UTC | 2026-06-14 20:09 UTC | 2h 56m |
| N797RJ |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-06-14 19:13 UTC | 2026-06-14 20:03 UTC | 50m |
| CPA829 | Cathay Pacific | Toronto Pearson International Airport (CYYZ) | Zhuhai Airport (ZGSD) | 2026-06-14 05:59 UTC | 2026-06-14 20:01 UTC | 14h 2m |
| DAL63 | Delta Air Lines | Madrid Barajas International Airport (LEMD) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-14 12:57 UTC | 2026-06-14 20:00 UTC | 7h 2m |
| XBSCW | XBS | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-06-14 19:39 UTC | 2026-06-14 20:00 UTC | 20m |
| N812MJ |  | Boerne Stage Airfield (K5C1) | Boerne Stage Airfield (K5C1) | 2026-06-14 19:41 UTC | 2026-06-14 19:55 UTC | 13m |
| CPA085 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-06-14 04:57 UTC | 2026-06-14 19:50 UTC | 14h 52m |
| CASH31 | CAS | Perot Field/Fort Worth Alliance Airport (KAFW) | Flying Bull Ranch Airport (TA52) | 2026-06-14 18:35 UTC | 2026-06-14 19:46 UTC | 1h 11m |
| N363D |  | Gulfport-Biloxi International Airport (KGPT) | Owen Field (4XA3) | 2026-06-14 17:25 UTC | 2026-06-14 19:46 UTC | 2h 21m |
| N421MQ |  | Orange County Airport (KMGJ) | Waterbury-Oxford Airport (KOXC) | 2026-06-14 18:40 UTC | 2026-06-14 19:41 UTC | 1h 1m |
| N682AC |  | Salaika Aviation Airport (07TA) | Bb Airpark (TE88) | 2026-06-14 19:13 UTC | 2026-06-14 19:41 UTC | 28m |
| N680EA |  | Birmingham-Shuttlesworth International Airport (KBHM) | WV23 (WV23) | 2026-06-14 18:38 UTC | 2026-06-14 19:39 UTC | 1h 1m |
| FTO388 | FTO | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-06-14 19:03 UTC | 2026-06-14 19:36 UTC | 32m |
| N6802P |  | Whiteman Airport (KWHP) | Whiteman Airport (KWHP) | 2026-06-14 19:30 UTC | 2026-06-14 19:32 UTC | 2m |
| N566KB |  | Hurlburt Field (KHRT) | TA16 (TA16) | 2026-06-14 17:21 UTC | 2026-06-14 19:31 UTC | 2h 10m |
| FRG100 | FRG | Chicago Executive Airport (KPWK) | Lehigh Valley International Airport (KABE) | 2026-06-14 17:48 UTC | 2026-06-14 19:31 UTC | 1h 42m |
| RYR70QN | Ryanair | Trieste / Ronchi Dei Legionari (LIPQ) | Olbia / Costa Smeralda Airport (LIEO) | 2026-06-14 18:36 UTC | 2026-06-14 19:27 UTC | 51m |
| N65DJ |  | Linden Airport (KLDJ) | Teterboro Airport (KTEB) | 2026-06-14 19:13 UTC | 2026-06-14 19:24 UTC | 10m |
| USC101 | USC | Charlotte/Douglas International Airport (KCLT) | Fulton County Executive/Charlie Brown Field (KFTY) | 2026-06-14 18:44 UTC | 2026-06-14 19:22 UTC | 38m |
| KATT72 | KAT | Pensacola International Airport (KPNS) | Ocean Springs Airport (K5R2) | 2026-06-14 18:59 UTC | 2026-06-14 19:21 UTC | 22m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
