# Exercise 2: 3D Stepped Pyramid with Three.js

## Description

Interactive 3D scene featuring a stepped pyramid constructed from multiple Box geometries with PBR materials, advanced lighting, and camera controls.

## CodeSandbox Link

**Project Name**: `piramide-[Juan David Ramírez Torres]`  
**Template Base**: Three.js Basic Example  
[Live Demo - [CodeSandbox](https://codesandbox.io/p/devbox/hopeful-hooks-ht88l6?workspaceId=ws_FJjALXsLhwXHNKHrZjCXRB)]

## Implementation

### Pyramid Architecture

- **5-Level Structure**: Decreasing box count per level (base to apex)
- **Grid Layout**: Boxes arranged in systematic grid patterns
- **Geometric Progression**: Each level 40% smaller than the previous
- **Individual Positioning**: Precise placement with slight randomization for organic appearance

### PBR Material System

- **Diffuse Textures**: Brick pattern for realistic surface appearance
- **Normal Mapping**: Surface detail enhancement for depth illusion
- **Roughness Mapping**: Material property variation across surfaces
- **Level Variations**: Different material properties per pyramid level
- **Color Gradation**: HSL color shifts from base to apex

### Advanced Lighting Setup

- **Directional Light**: Primary illumination simulating sunlight with shadow casting
- **Ambient Light**: Global illumination for realistic lighting balance
- **Fill Light**: Secondary directional light for shadow detail preservation
- **Point Light**: Accent lighting for dramatic visual enhancement
- **Shadow Configuration**: High-resolution soft shadows (2048x2048 maps)

### Interactive Features

- **OrbitControls**: Smooth camera manipulation with damping
- **Responsive Design**: Automatic viewport adjustment
- **Subtle Animation**: Gentle pyramid rotation based on time
- **Atmospheric Effects**: Floating particle system for visual enhancement

## Technical Specifications

### Core Technologies

- **Three.js r128**: 3D graphics rendering engine
- **ES6 Modules**: Modern JavaScript import system
- **WebGL Renderer**: Hardware-accelerated 3D graphics
- **Shadow Mapping**: Real-time shadow calculation

### Performance Optimizations

- **Efficient Geometry**: Optimized box geometry reuse
- **Texture Management**: Proper texture wrapping and configuration
- **Render Optimization**: Selective shadow casting and receiving
- **Memory Management**: Proper cleanup and resource handling

### Visual Enhancements

- **Tone Mapping**: ACES Filmic tone mapping for cinematic appearance
- **Anti-aliasing**: Smooth edge rendering
- **Post-processing**: Enhanced visual quality through renderer configuration

## Scene Composition

- **Ground Plane**: Large reception surface for pyramid shadows
- **Particle System**: 100 floating particles for atmospheric depth
- **Color Palette**: Coordinated earth tones with blue accent lighting
- **Spatial Organization**: Balanced composition with proper scale relationships

## Interaction Controls

- **Mouse Orbit**: Left-click drag for camera rotation
- **Zoom**: Mouse wheel for distance adjustment
- **Pan**: Right-click drag for camera translation
- **Constraints**: Bounded interaction to maintain optimal viewing angles

## Files Structure

- `index.js`: Main implementation file
- `captura.png`: Scene screenshot for documentation

## Development Notes

The implementation prioritizes visual impact while maintaining educational clarity. The stepped pyramid design showcases fundamental 3D programming concepts including geometric transformation, material application, lighting calculation, and interactive camera control.

**Performance**: Optimized for smooth 60fps rendering on modern browsers with hardware acceleration enabled.
