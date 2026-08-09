# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_16:48:41_UTC-green)

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

**Latest saved flight:** 2026-08-09 16:48:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 16:48:41 UTC

- **181,711** saved flights
- **58,023** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **181,711** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,183,785.7 tonnes** estimated CO2 emissions
- **126,596,271 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7207 |
| 2 | SkyWest Airlines | 6598 |
| 3 | EJA | 3569 |
| 4 | IndiGo | 3192 |
| 5 | Southwest Airlines | 2848 |
| 6 | American Airlines | 2824 |
| 7 | ENY | 2259 |
| 8 | Delta Air Lines | 2149 |
| 9 | LATAM Airlines | 1699 |
| 10 | AZU | 1626 |
| 11 | Lufthansa | 1616 |
| 12 | WIF | 1506 |
| 13 | Vueling | 1505 |
| 14 | LXJ | 1415 |
| 15 | Swiss International | 1245 |
| 16 | easyJet | 1243 |
| 17 | AXM | 1226 |
| 18 | QLK | 1116 |
| 19 | EJU | 1112 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1097 |
| 22 | VIV | 998 |
| 23 | GLO | 973 |
| 24 | CXK | 949 |
| 25 | AEE | 948 |
| 26 | Cathay Pacific | 947 |
| 27 | Air France | 943 |
| 28 | United Airlines | 931 |
| 29 | PGT | 919 |
| 30 | MXY | 909 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 155292 |
| 2 | 🇪🇸 ES | 11709 |
| 3 | 🇧🇷 BR | 10436 |
| 4 | 🇦🇺 AU | 10202 |
| 5 | 🇮🇳 IN | 10000 |
| 6 | 🇨🇦 CA | 9882 |
| 7 | 🇮🇹 IT | 9413 |
| 8 | 🇩🇪 DE | 9017 |
| 9 | 🇬🇧 GB | 8407 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7254 |
| 12 | 🇨🇴 CO | 6753 |
| 13 | 🇬🇷 GR | 5330 |
| 14 | 🇲🇽 MX | 5184 |
| 15 | 🇨🇭 CH | 4857 |
| 16 | 🇹🇷 TR | 4706 |
| 17 | 🇳🇴 NO | 4685 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3055 |
| 20 | 🇿🇦 ZA | 3015 |
| 21 | 🇹🇭 TH | 2804 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2311 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1838 |
| 27 | 🇭🇷 HR | 1811 |
| 28 | 🇲🇪 ME | 1646 |
| 29 | 🇳🇱 NL | 1635 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3749 |
| 2 | Denver International Airport |  | US | 2995 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2233 |
| 5 | Guaymaral Airport |  | CO | 2230 |
| 6 | Harry Reid International Airport |  | US | 2129 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1957 |
| 8 | Zurich Airport |  | CH | 1941 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1882 |
| 10 | La Aurora Airport |  | GT | 1774 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1652 |
| 12 | Chicago O'Hare International Airport |  | US | 1631 |
| 13 | El Dorado International Airport |  | CO | 1621 |
| 14 | Salt Lake City International Airport |  | US | 1618 |
| 15 | Frankfurt am Main International Airport |  | DE | 1581 |
| 16 | Macau International Airport |  | MO | 1518 |
| 17 | Congonhas Airport |  | BR | 1514 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1440 |
| 19 | Madrid Barajas International Airport |  | ES | 1432 |
| 20 | Capua Airport |  | IT | 1420 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1356 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1298 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1254 |
| 25 | Charles de Gaulle International Airport |  | FR | 1240 |
| 26 | Charlotte/Douglas International Airport |  | US | 1229 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Ninoy Aquino International Airport |  | PH | 1135 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1128 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1110 |
| 32 | Barcelona International Airport |  | ES | 1080 |
| 33 | Viracopos International Airport |  | BR | 1045 |
| 34 | Seattle-Tacoma International Airport |  | US | 1043 |
| 35 | Daniel K Inouye International Airport |  | US | 1042 |
| 36 | Reno/Tahoe International Airport |  | US | 1035 |
| 37 | Calgary International Airport |  | CA | 1030 |
| 38 | Oslo Gardermoen Airport |  | NO | 1009 |
| 39 | Tenerife Norte Airport |  | ES | 993 |
| 40 | Vitoria/Foronda Airport |  | ES | 987 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 920 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 670 | 21m | 244 km | 2,821.2 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 419 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 256 | 1h 48m | 1,423 km | 6,282.6 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 247 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 242 | 20m | 250 km | 1,045.3 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 223 | 19m | 99 km | 382.0 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 221 | 1h 15m | 961 km | 3,663.2 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 219 | 31m | 49 km | 185.1 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 218 | 50m | 556 km | 2,089.7 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 217 | 19m | 144 km | 539.8 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 214 | 1h 38m | 1,156 km | 4,269.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 213 | 24m | 218 km | 802.5 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 204 | 28m | 152 km | 533.1 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 197 | 1h 1m | 695 km | 2,361.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SWR1ZB | Swiss International | Eleftherios Venizelos International Airport (LGAV) | Zurich Airport (LSZH) | 2026-08-09 14:20 UTC | 2026-08-09 16:48 UTC | 2h 27m |
| N492SF |  | Jim & Julie's Airport (96WA) | Jim & Julie's Airport (96WA) | 2026-08-09 15:52 UTC | 2026-08-09 16:39 UTC | 47m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-09 16:23 UTC | 2026-08-09 16:37 UTC | 14m |
| N4174L |  | Chicago Midway International Airport (KMDW) | Chicago Midway International Airport (KMDW) | 2026-08-09 15:13 UTC | 2026-08-09 16:37 UTC | 1h 23m |
| N399TT |  | Windshear Airport (63NY) | Windshear Airport (63NY) | 2026-08-09 16:16 UTC | 2026-08-09 16:37 UTC | 20m |
| N87Q |  | Meadow Airport (07VT) | Shaw Meadow Airport (VT52) | 2026-08-09 16:08 UTC | 2026-08-09 16:36 UTC | 27m |
| N57GW |  | Sierra Vista Municipal-Libby Army Air Field (KFHU) | Montezuma Airport (19AZ) | 2026-08-09 15:23 UTC | 2026-08-09 16:34 UTC | 1h 11m |
| MILAN75 | MIL | Rodez-Marcillac Airport (LFCR) | Aubenas-Ardeche Meridional Airport (LFHO) | 2026-08-09 16:17 UTC | 2026-08-09 16:31 UTC | 14m |
| N191TW |  | Livermore Municipal Airport (KLVK) | Blue Canyon - Nyack Airport (KBLU) | 2026-08-09 15:19 UTC | 2026-08-09 16:27 UTC | 1h 7m |
| N734ZY |  | Denton Enterprise Airport (KDTO) | Tightwaad Air Ranch Airport (XA16) | 2026-08-09 15:34 UTC | 2026-08-09 16:25 UTC | 50m |
| 0000000 |  | KL47 (KL47) | Allen Parish Airport (KACP) | 2026-08-09 16:08 UTC | 2026-08-09 16:24 UTC | 16m |
| N819BB |  | Plymouth Municipal Airport (KPYM) | Laguardia Airport (KLGA) | 2026-08-09 15:09 UTC | 2026-08-09 16:23 UTC | 1h 13m |
| N237RE |  | Minden-Tahoe Airport (KMEV) | Lake Tahoe Airport (KTVL) | 2026-08-09 16:16 UTC | 2026-08-09 16:23 UTC | 6m |
| N739EZ |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-08-09 15:58 UTC | 2026-08-09 16:22 UTC | 23m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-09 16:10 UTC | 2026-08-09 16:17 UTC | 6m |
| 5YSLL |  | Nairobi Wilson Airport (HKNW) | Jomo Kenyatta International Airport (HKJK) | 2026-08-09 16:07 UTC | 2026-08-09 16:17 UTC | 9m |
| N87JF |  | Lake Wales Municipal Airport (KX07) | Lake Wales Municipal Airport (KX07) | 2026-08-09 15:29 UTC | 2026-08-09 16:16 UTC | 46m |
| N1293E |  | Airglades Airport (K2IS) | Airglades Airport (K2IS) | 2026-08-09 15:56 UTC | 2026-08-09 16:15 UTC | 19m |
| N735RK |  | Cherokee Ranch Airport (OK25) | Gregg Airport (7OK1) | 2026-08-09 15:57 UTC | 2026-08-09 16:13 UTC | 16m |
| CFR608 | CFR | Chino Airport (KCNO) | Corona Municipal Airport (KAJO) | 2026-08-09 15:52 UTC | 2026-08-09 16:13 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
