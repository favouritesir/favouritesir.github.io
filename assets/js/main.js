/**
 * Ashikur Rahman (favouritesir.me) Portfolio Engine
 * Three.js 3D Background, Parallax & Micro-Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initTypewriter();
  initHeroCardTilt();
  initThreeBackground();
});

/* ==========================================================================
   1. NAVBAR & NAVIGATION
   ========================================================================== */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  const navToggle = document.getElementById('nav-toggle');
  const navLinks = document.getElementById('nav-links');
  const links = document.querySelectorAll('.nav-link');

  // Sticky Navbar on Scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
    highlightCurrentSection();
  });

  // Mobile Toggle
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });

    links.forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
      });
    });
  }

  // Active Link Tracking
  function highlightCurrentSection() {
    const sections = document.querySelectorAll('section[id]');
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120;
      const sectionId = current.getAttribute('id');
      const activeLink = document.querySelector(`.nav-link[href*="${sectionId}"]`);

      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        links.forEach(l => l.classList.remove('active'));
        if (activeLink) activeLink.classList.add('active');
      }
    });
  }
}

/* ==========================================================================
   2. TYPEWRITER EFFECT
   ========================================================================== */
function initTypewriter() {
  const typedTarget = document.getElementById('typed-text');
  if (!typedTarget) return;

  const phrases = [
    'Algorithm Researcher',
    'Conceived Cloud Sort (DOI: 10.5281/zenodo.23665548)',
    'In-Place Infix-to-Prefix (DOI: 10.5281/zenodo.23657544)',
    'Full-Stack & Systems Engineer',
    'Embedded IoT & Serverless Architect'
  ];

  let phraseIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let typingSpeed = 70;

  function type() {
    const currentPhrase = phrases[phraseIndex];

    if (isDeleting) {
      typedTarget.textContent = currentPhrase.substring(0, charIndex - 1);
      charIndex--;
      typingSpeed = 35;
    } else {
      typedTarget.textContent = currentPhrase.substring(0, charIndex + 1);
      charIndex++;
      typingSpeed = 75;
    }

    if (!isDeleting && charIndex === currentPhrase.length) {
      isDeleting = true;
      typingSpeed = 1800; // Pause at full phrase
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      typingSpeed = 400; // Pause before next phrase
    }

    setTimeout(type, typingSpeed);
  }

  type();
}

/* ==========================================================================
   3. 3D HERO CARD MOUSE TILT
   ========================================================================== */
function initHeroCardTilt() {
  const card = document.getElementById('hero-card');
  if (!card) return;

  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    
    const rotateX = ((y - centerY) / centerY) * -12;
    const rotateY = ((x - centerX) / centerX) * 12;

    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
  });

  card.addEventListener('mouseleave', () => {
    card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
  });
}

/* ==========================================================================
   4. THREE.JS 3D BACKGROUND & PARALLAX SCROLL
   ========================================================================== */
function initThreeBackground() {
  const canvas = document.getElementById('bg-canvas');
  if (!canvas || typeof THREE === 'undefined') return;

  // Scene & Camera
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(65, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 40;

  // Renderer
  const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true,
    antialias: true,
    powerPreference: 'high-performance'
  });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Ambient Lighting
  const ambientLight = new THREE.AmbientLight(0x0a192f, 2.5);
  scene.add(ambientLight);

  const pointLight1 = new THREE.PointLight(0x00f0ff, 3, 100);
  pointLight1.position.set(20, 20, 25);
  scene.add(pointLight1);

  const pointLight2 = new THREE.PointLight(0x818cf8, 2.5, 100);
  pointLight2.position.set(-25, -20, 20);
  scene.add(pointLight2);

  // Group to hold all 3D objects for parallax rotation
  const universeGroup = new THREE.Group();
  scene.add(universeGroup);

  // --- Object 1: 3D Algorithm Polyhedron (Central Wireframe Icosahedron) ---
  const icoGeometry = new THREE.IcosahedronGeometry(12, 1);
  const icoMaterial = new THREE.MeshStandardMaterial({
    color: 0x00d2ff,
    wireframe: true,
    emissive: 0x00599c,
    emissiveIntensity: 0.35,
    roughness: 0.2,
    metalness: 0.8
  });
  const icosahedron = new THREE.Mesh(icoGeometry, icoMaterial);
  icosahedron.position.set(16, 2, -5);
  universeGroup.add(icosahedron);

  // --- Object 2: Surrounding Orbiting Torus Knot Ring ---
  const torusGeometry = new THREE.TorusGeometry(18, 0.25, 16, 100);
  const torusMaterial = new THREE.MeshBasicMaterial({
    color: 0x818cf8,
    transparent: true,
    opacity: 0.35,
    wireframe: true
  });
  const torusRing = new THREE.Mesh(torusGeometry, torusMaterial);
  torusRing.position.set(16, 2, -5);
  torusRing.rotation.x = Math.PI / 3;
  universeGroup.add(torusRing);

  // --- Object 3: 1,200 Interactive Particle Cloud (Algorithm Data Nodes) ---
  const particleCount = 1200;
  const particleGeometry = new THREE.BufferGeometry();
  const particlePositions = new Float32Array(particleCount * 3);
  const particleScales = new Float32Array(particleCount);

  for (let i = 0; i < particleCount * 3; i += 3) {
    particlePositions[i] = (Math.random() - 0.5) * 160;     // X
    particlePositions[i + 1] = (Math.random() - 0.5) * 160; // Y
    particlePositions[i + 2] = (Math.random() - 0.5) * 120; // Z
    particleScales[i / 3] = Math.random() * 2 + 0.5;
  }

  particleGeometry.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
  particleGeometry.setAttribute('scale', new THREE.BufferAttribute(particleScales, 1));

  // Custom particle shader-like glowing texture
  const particleCanvas = document.createElement('canvas');
  particleCanvas.width = 16;
  particleCanvas.height = 16;
  const pCtx = particleCanvas.getContext('2d');
  const gradient = pCtx.createRadialGradient(8, 8, 0, 8, 8, 8);
  gradient.addColorStop(0, 'rgba(56, 189, 248, 1)');
  gradient.addColorStop(0.4, 'rgba(0, 240, 255, 0.6)');
  gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
  pCtx.fillStyle = gradient;
  pCtx.fillRect(0, 0, 16, 16);

  const particleTexture = new THREE.CanvasTexture(particleCanvas);

  const particleMaterial = new THREE.PointsMaterial({
    size: 1.8,
    map: particleTexture,
    transparent: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
    color: 0x38bdf8
  });

  const particleSystem = new THREE.Points(particleGeometry, particleMaterial);
  universeGroup.add(particleSystem);

  // --- Mouse & Scroll Parallax State ---
  let mouseX = 0;
  let mouseY = 0;
  let targetX = 0;
  let targetY = 0;
  let scrollProgress = 0;

  window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX / window.innerWidth) * 2 - 1;
    mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
  });

  window.addEventListener('scroll', () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    scrollProgress = totalHeight > 0 ? window.scrollY / totalHeight : 0;
  });

  // Handle Resize
  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  });

  // --- Animation Loop ---
  let clock = new THREE.Clock();

  function animate() {
    requestAnimationFrame(animate);

    const elapsedTime = clock.getElapsedTime();

    // Smooth Lerp for Mouse Parallax
    targetX += (mouseX * 0.05 - targetX) * 0.05;
    targetY += (mouseY * 0.05 - targetY) * 0.05;

    // Rotate Polyhedron & Ring
    icosahedron.rotation.x = elapsedTime * 0.15;
    icosahedron.rotation.y = elapsedTime * 0.22;
    torusRing.rotation.z = elapsedTime * 0.1;
    torusRing.rotation.y = elapsedTime * 0.08;

    // Slowly rotate background particle constellation
    particleSystem.rotation.y = elapsedTime * 0.03;
    particleSystem.rotation.x = elapsedTime * 0.015;

    // Scroll-driven camera parallax movement
    camera.position.x += (targetX * 25 - camera.position.x) * 0.05;
    camera.position.y += (-targetY * 25 - scrollProgress * 15 - camera.position.y) * 0.05;
    camera.position.z = 40 + Math.sin(scrollProgress * Math.PI) * 10;

    camera.lookAt(0, -scrollProgress * 10, 0);

    renderer.render(scene, camera);
  }

  animate();
}
